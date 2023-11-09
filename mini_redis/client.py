import requests
import pickle


class MiniRedisClient:
    def __init__(self, server_url: str):
        self.server_url = server_url

    def __getitem__(self, key: str):
        response = requests.get(f"{self.server_url}/get/{key}")
        if response.status_code == 200:
            return response.json()['value']
        else:
            raise KeyError('Key not found')

    def __setitem__(self, key: str, value):
        response = requests.post(f"{self.server_url}/set/{key}", data=value)
        if response.status_code != 200:
            raise Exception('Failed to set value')

    def __delitem__(self, key: str):
        response = requests.delete(f"{self.server_url}/delete/{key}")
        if response.status_code != 200:
            raise KeyError('Key not found')

