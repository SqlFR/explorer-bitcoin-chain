import os

# Path to the local environment file (same directory as this config.py)
ENV_FILE_PATH = os.path.join(os.path.dirname(__file__), "env.local")

def _load_env_file(path: str = ENV_FILE_PATH) -> None:
    """
    Charge les variables d'environnement depuis un fichier de type:
        KEY=VALUE
    Les variables déjà présentes dans os.environ NE sont PAS écrasées.
    """
    if not os.path.exists(path):
        return

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)
            key, value = key.strip(), value.strip()

            if key and key not in os.environ:
                os.environ[key] = value

# Charge automatiquement env.local avant de lire les variables
_load_env_file()

def _get_env(name: str, default: str | None = None) -> str:
    value = os.environ.get(name)
    if value is None:
        if default is not None:
            return default
        raise RuntimeError(f"Variable d'environnement {name} manquante")
    return value

# Configuration RPC
RPC_CONFIG: dict[str, str] = {
    'rpc_user': _get_env("BITCOIN_RPC_USER", 'main'),
    'rpc_password': _get_env("BITCOIN_RPC_PASSWORD"),
    'rpc_host': _get_env("BITCOIN_RPC_HOST",'192.168.2.57'),
    'rpc_port': _get_env("BITCOIN_RPC_PORT",'8332'),
}
