from zabbix_api.http_request import http_post
from zabbix_api import script_name, media_name, action_name, ACTION_MESSAGE_BODY
from zabbix_api.get_token import user_login

token = user_login()


def mediatype_get():
    """
    获取mediatype
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "mediatype.get",
        "params": {
            "output": "mediatypeid",
            "filter": {"description": media_name},
        },
        "auth": token,
        "id": 1,
    }
    resp = http_post(data=payload)
    print('get mediatype', resp)
    return [i["mediatypeid"] for i in resp["result"]]


def mediatype_delete(media_type_ids):
    """
    删除mediatype
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "mediatype.delete",
        "params": media_type_ids,
        "auth": token,
        "id": 1,
    }
    resp = http_post(data=payload)
    print('delete mediatype', resp)


def mediatype_create():
    """
    创建脚本
    """
    exec_params = [
        # '{ALERT.SUBJECT}',
        "{ALERT.MESSAGE}",
    ]
    payload = {
        "jsonrpc": "2.0",
        "method": "mediatype.create",
        "params": {
            "name": media_name,
            "description": media_name,
            "exec_path": script_name,
            "exec_params": "\r\n".join(exec_params) + "\r\n",
            "type": 1,
            "status": 0,
            "message_templates": [
                {
                    "eventsource": 0,
                    "recovery": 0,
                    "subject": action_name + " {TRIGGER.NAME}: {TRIGGER.STATUS}",
                    "message": ACTION_MESSAGE_BODY,
                }
            ],
        },
        "auth": token,
        "id": 1,
    }
    resp = http_post(data=payload)
    print('create mediatype', resp)


if __name__ == '__main__':
    mediatype_ids = mediatype_get()
    mediatype_delete(mediatype_ids)
    mediatype_create()
