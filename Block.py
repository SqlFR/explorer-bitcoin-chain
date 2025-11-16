from call_rpc import call_rpc

class Block:
    """Représentation d'un bloc Bitcoin identifié par son hash."""
    def __init__(self, hash_block: str) -> None:
        """
        :param hash_block: Hash du bloc (chaîne hexadécimale).
        """
        self.hash_block = hash_block

    def get_block(self, verbosity: int=0) -> dict:
        """
        Retourne les données du bloc.

        :param verbosity: Niveau de détail (0, 1 ou 2 selon l'API).
        :return: Réponse JSON sous forme de dict.
        """
        return call_rpc(self.hash_block,'getblock', [self.hash_block, verbosity])

    def get_blockhash(self) -> str:
        """Retourne le hash du bloc."""
        return self.hash_block

    def get_blockheader(self) -> dict:
        """Retourne le header du bloc."""
        return call_rpc(self.hash_block,"getblockheader", [self.hash_block])

    def get_blockstats(self, values: str | list[str] | None=None) -> dict:
        """
        Retourne les statistiques du bloc.

        :param values: Liste de champs spécifiques à demander, ou None pour tous.
        :return: Réponse JSON sous forme de dict.
        """
        if not values:
            values = []

        return call_rpc(self.hash_block,"getblockstats", [self.hash_block, values])
