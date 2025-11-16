class BlockError(Exception):
    """Erreur générique liée aux opérations sur un bloc."""

class BlockNotFoundError(BlockError):
    """Bloc introuvable sur le nœud."""

class RpcError(BlockError):
    """Erreur renvoyée par le nœud RPC."""