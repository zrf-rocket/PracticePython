from zabbix_api.get_token import user_login, http_post

def event_get():
    payload = {
        "jsonrpc": "2.0", "method": "event.get",
        "params": {
            "output": "extend",
            "select_acknowledges": "extend",
            "selectTags": "extend",
            "selectSuppressionData": "extend",
            "objectids": "13926",
            "sortfield": ["clock", "eventid"],
            "sortorder": "DESC"
        },
        "id": 1,
        "auth": user_login()
    }
    resp = http_post(data=payload)
    print('event_get', resp)


if __name__ == '__main__':
    event_get()
