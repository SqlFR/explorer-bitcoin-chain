import requests
from requests_node import send_rpc_request
from errors import BlockError, BlockNotFoundError, RpcError


def call_rpc(method: str, params: list | None = None):
    """
    Appelle le RPC sous-jacent, gère les erreurs réseau/HTTP et normalise
    les erreurs JSON-RPC en exceptions métier BlockError.

    :param method: Nom de la méthode JSON-RPC (ex: "getblock").
    :param params: Paramètres passés à la méthode RPC.
    :return: Champ "result" de la réponse JSON-RPC.
    :raises BlockError: Erreur réseau, réponse invalide ou erreur RPC.
    """

    if params is None:
        params = []

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
            raise BlockNotFoundError(f"Bloc introuvable: ({message})")
        else:
            raise RpcError(f"Erreur RPC '{method}' (code {code}): {message}")

    return response.get("result")