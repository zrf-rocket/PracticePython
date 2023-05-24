from zabbix_api import url, username, password
from pyzabbix import ZabbixAPI

zapi = ZabbixAPI(url)
zapi.login(username, password)

hosts = zapi.host.get(output="extend")
for host in hosts:
    print(host)
    print(host["hostid"], host["host"])
