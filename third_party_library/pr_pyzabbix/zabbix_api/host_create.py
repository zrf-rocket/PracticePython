from zabbix_api.get_token import user_login, http_post

def host_create():
    """
    批量创建主机
    """
    for index in range(100):
        payload = {
            "jsonrpc": "2.0",
            "method": "host.create",
            "params": {
                "host": f"server-{index}",
                "interfaces": [
                    {
                        "type": 1,
                        "main": 1,
                        "useip": 1,
                        "ip": "192.168.1.130",
                        "dns": "",
                        "port": "10050"
                    }
                ],
                "groups": [
                    {
                        "groupid": "2"
                    }
                ],
                "templates": [
                    {
                        "templateid": "10001"
                    }
                ]
            },
            "id": 2,
            "auth": user_login()
        }
        resp = http_post(data=payload)
        print('create mediatype', resp)

if __name__ == '__main__':
    host_create()