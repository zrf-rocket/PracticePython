from zabbix_api.http_request import http_post
from zabbix_api import password, usrgrpid, script_name, media_name, user_name, action_name, ACTION_MESSAGE_BODY
from zabbix_api.get_token import user_login
from zabbix_api.api_mediatype import mediatype_get

token = user_login()


def user_get():
    """
    获取以前老的mediatype
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "user.get",
        "params": {
            "output": "userid",
            "filter": {"alias": user_name},
        },
        "auth": token,
        "id": 1,
    }
    resp = http_post(data=payload)
    print('get user', resp)
    return [i["userid"] for i in resp["result"]]


def user_delete(user_ids):
    """
    删除mediatype
    """
    payload = {"jsonrpc": "2.0", "method": "user.delete", "params": user_ids, "auth": token, "id": 1}
    resp = http_post(data=payload)
    print("delete user", resp)


def user_create():
    """创建用户"""
    mediatypeid = mediatype_get()[0]
    if mediatypeid and isinstance(mediatypeid, list):
        mediatypeid = mediatypeid[0]
    payload = {
        "jsonrpc": "2.0",
        "method": "user.create",
        "params": {
            "alias": user_name,
            "name": user_name,
            "surname": user_name,
            "passwd": password,
            "type": 3,  # Zabbix super admin
            "usrgrps": [{"usrgrpid": usrgrpid}],
            "user_medias": [
                {
                    "mediatypeid": mediatypeid,
                    "sendto": user_name,
                    "active": 0,
                    "severity": 63,  # all severity
                    "period": "1-7,00:00-24:00",
                }
            ],
        },
        "auth": token,
        "id": 1,
    }
    resp = http_post(data=payload)
    print('create user', resp)


if __name__ == '__main__':
    user_ids = user_get()
    user_delete(user_ids)
    user_create()
