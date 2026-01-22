from call_rpc import call_rpc
from HashBase import HashBase

class Block:
    """Représentation d'un bloc Bitcoin identifié par son hash."""
    def __init__(self, hash_block: HashBase) -> None:
        """
        :param hash_block: Hash du bloc en bytes.
        """
        self.hash_block = hash_block

    def _hex(self):
        """Hash sous ferme hexadécimal."""
        return self.hash_block.to_hex()

    def get_block(self, verbosity: int=0):
        """
        Retourne les données du bloc.

        :param verbosity: Niveau de détail (0, 1 ou 2 selon l'API).
        :return: Réponse JSON sous forme de dict.
        """
        return call_rpc('getblock', [self._hex(), verbosity])

    def get_blockhash(self) -> str:
        return self._hex()

    def get_blockheader(self):
        return call_rpc("getblockheader", [self._hex()])

    def get_blockstats(self, values: str | list[str] | None = None):
        """
        :param values: Liste de champs spécifiques à demander, ou None pour tous.
        :return: Réponse JSON sous forme de dict.
        """
        if values is None:
            return call_rpc("getblockstats", [self._hex()])

        if isinstance(values, str):
            values = [values]

        return call_rpc("getblockstats", [self._hex(), values])
