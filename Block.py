import requests
from requests_node import send_rpc_request

class BlockError(Exception):
    """Erreur générique liée aux opérations sur un bloc."""

class BlockNotFoundError(BlockError):
    """Bloc introuvable sur le nœud."""

class RpcError(BlockError):
    """Erreur renvoyée par le nœud RPC."""

class Block:
    """Représentation d'un bloc Bitcoin identifié par son hash."""
    def __init__(self, hash_block: str) -> None:
        """
        :param hash_block: Hash du bloc (chaîne hexadécimale).
        """
        self.hash_block = hash_block

    def _call_rpc(self, method: str, params: list[str]) -> dict:
        """
        Appelle le RPC sous-jacent, gère les erreurs réseau/HTTP et normalise
        les erreurs JSON-RPC en exceptions métier BlockError.

        :param method: Nom de la méthode JSON-RPC (ex: "getblock").
        :param params: Paramètres passés à la méthode RPC.
        :return: Champ "result" de la réponse JSON-RPC.
        :raises BlockError: Erreur réseau, réponse invalide ou erreur RPC.
        """
        try:
            response = send_rpc_request({"method": method, "params": params})
        except requests.exceptions.RequestException as e:
            # Erreurs réseau, timeout,HTTP non 2xx, etc.
            raise BlockError(f"Erreur réseau lors de l'appel RPC '{method}': {e}") from e

        if not isinstance(response, dict):
            raise RpcError(f"Réponse RPC invalide pour '{method}': {response!r}, {type(response)}")

        error = response.get("error")
        if error:
            code = error.get("code")
            message = error.get("message", "Erreur RPC inconnue")

            # Exemple: code -5 = bloc non trouvé (Bitcoin Core)
            if code in (-5, -8):
                raise BlockNotFoundError(f"Bloc introuvable: {self.hash_block} ({message})")
            else:
                raise RpcError(f"Erreur RPC '{method}' (code {code}): {message}")

        return response.get("result")

    def get_block(self, verbosity: int=0) -> dict:
        """
        Retourne les données du bloc.

        :param verbosity: Niveau de détail (0, 1 ou 2 selon l'API).
        :return: Réponse JSON sous forme de dict.
        """
        return self._call_rpc('getblock', [self.hash_block, verbosity])

    def get_blockhash(self) -> str:
        """Retourne le hash du bloc."""
        return self.hash_block

    def get_blockheader(self) -> dict:
        """Retourne le header du bloc."""
        return self._call_rpc("getblockheader", [self.hash_block])

    def get_blockstats(self, values: str | list[str] | None=None) -> dict:
        """
        Retourne les statistiques du bloc.

        :param values: Liste de champs spécifiques à demander, ou None pour tous.
        :return: Réponse JSON sous forme de dict.
        """
        if not values:
            values = []

        return self._call_rpc("getblockstats", [self.hash_block, values])
