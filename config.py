import os

def _get_env(name: str, default: str | None = None) -> str:
    value = os.environ.get(name)
    if value is None:
        if default is not None:
            return default
        raise RuntimeError(f"Variable d'environnement {name} manquante")
    return value

# Configuration RPC
RPC_CONFIG: dict[str, str] = {
    'rpc_user': _get_env("BITCOIN_RPC_USER", 'sql'),
    'rpc_password': _get_env("BITOIN_RPC_PASSWORD"),
    'rpc_host': _get_env("BITOIN_RPC_HOST",'192.168.2.57'),
    'rpc_port': _get_env("BITOIN_RPC_PORT",'8332'),
}