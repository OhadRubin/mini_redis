import requests
import json


class MiniRedisClient:
    def __init__(self, server_url: str):
        self.server_url = server_url

    def __getitem__(self, key: str):
        response = requests.get(f"{self.server_url}/get/{key}")
        if response.status_code == 200:
            return json.loads(response.json()['value'])
        else:
            raise KeyError('Key not found')
        
    def get(self, key: str, default=None):
        response = requests.get(f"{self.server_url}/get/{key}")
        if response.status_code == 200:
            return json.loads(response.json()['value'])
        else:
            raise default

    def __setitem__(self, key: str, value):
        response = requests.post(f"{self.server_url}/set/{key}", data=json.dumps(value))
        if response.status_code != 200:
            raise Exception('Failed to set value')

    def __delitem__(self, key: str):
        response = requests.delete(f"{self.server_url}/delete/{key}")
        if response.status_code != 200:
            raise KeyError('Key not found')

    def __contains__(self, key: str):
        response = requests.get(f"{self.server_url}/exists/{key}")
        return response.json()['exists']

    def keys(self):
        response = requests.get(f"{self.server_url}/keys")
        return response.json()['keys']

    def values(self):
        response = requests.get(f"{self.server_url}/values")
        return [json.loads(x) for x in response.json()['values']]

    def items(self):
        response = requests.get(f"{self.server_url}/items")
        return [(k,json.loads(v)) for k,v in response.json()['items']]

    def clear(self):
        response = requests.delete(f"{self.server_url}/clear")
        if response.status_code != 200:
            raise Exception('Failed to clear database')