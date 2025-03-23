import qbittorrentapi
from . import config

def connect_client():
    client = qbittorrentapi.Client(
        host=f'http://{config.QB_HOST}:{config.QB_PORT}',
        username=config.QB_USERNAME,
        password=config.QB_PASSWORD
    )
    client.auth_log_in()
    return client

def add_torrent(client, magnet_link):
    client.torrents_add(urls=magnet_link)

def get_status(client):
    return [(t.name, t.state, round(t.progress * 100)) for t in client.torrents_info()]

