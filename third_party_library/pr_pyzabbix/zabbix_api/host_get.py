import requests
from get_token import user_login
from zabbix_api import url
headers = {'Content-Type': 'application/json-rpc'}

data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid", "host"],
        "selectInterfaces": ['interfaceid', "ip"]
    },
    "auth": user_login(),
    "id": 1
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
