import requests
from requests.auth import HTTPBasicAuth
from config import RPC_CONFIG


# Recupere infos demandé en renseignant method et params
def send_rpc_request(payload) -> dict:
    """
    Envoie une requête JSON-RPC au noeud Bitcoin et retourne la réponse JSON complète.

    :param payload: Dictionnaire contenant au minimum "method" et "params".
    :return: Réponse JSON complète sous forme de dict ({"result": ..., "error": ..., "id": ...}).
    :raises requests.exceptions.RequestException: en cas d'erreur réseau/HTTP.
    """
    url = f"http://{RPC_CONFIG['rpc_host']}:{RPC_CONFIG['rpc_port']}/"
    # Met a jour le payload
    payload = {"jsonrpc": "1.0", "id": "py"} | payload

    r = requests.post(
        url,
        json=payload,
        auth=HTTPBasicAuth(RPC_CONFIG['rpc_user'], RPC_CONFIG['rpc_password']),
        timeout=30
    )

    # Lève une exception si HTTP != 2xx (c'est bien que ça remonte jusqu'à Block._call_rpc)
    r.raise_for_status()

    data = r.json()

    if not isinstance(data, dict):
        raise ValueError(f"Réponse JSON innattendue: {data!r}")

    return data
