from zabbix_api.http_request import http_post
from zabbix_api import script_name, media_name, user_name, action_name, ACTION_MESSAGE_BODY
from zabbix_api.get_token import user_login
from zabbix_api.api_mediatype import mediatype_get
from zabbix_api.api_user import user_get

token = user_login()
PARAM = int("11")


def action_get():
    payload = {
        "jsonrpc": "2.0",
        "method": "action.get",
        "params": {
            "output": "actionids",
            "filter": {"name": action_name},
        },
        "auth": token,
        "id": 1,
    }
    resp = http_post(data=payload)
    print('get action', resp)
    return [i["actionid"] for i in resp["result"]]


def action_delete(action_ids):
    """
    删除mediatype
    """
    payload = {"jsonrpc": "2.0", "method": "action.delete", "params": action_ids, "auth": token, "id": 1}
    resp = http_post(data=payload)
    print('delete action', resp)


def action_create():
    """创建触发器"""
    userid = user_get()
    if userid and isinstance(userid, list):
        userid = userid[0]
    mediatypeid = mediatype_get()
    if mediatypeid and isinstance(mediatypeid, list):
        mediatypeid = mediatypeid[0]
    payload = {
        "jsonrpc": "2.0",
        "method": "action.create",
        "params": {
            "name": action_name,
            "eventsource": 0,
            "status": 0,
            "esc_period": 3600,
            "def_shortdata": action_name + " {TRIGGER.NAME}: {TRIGGER.STATUS}",
            "def_longdata": ACTION_MESSAGE_BODY,
            "filter": {
                "evaltype": 0,  # and/or
                "conditions": [
                    {
                        "conditiontype": 16,  # version 3.x is Maintenance status,4.0 is Problem is suppressed
                        "operator": PARAM,  # not in or No
                        "value": "",  # must be empty
                    },
                    # zabbix 3.2/3.4 don't have trigger value
                    # {
                    #     "conditiontype": 5,  # trigger value
                    #     "operator": 0,  # =
                    #     "value": 1  # problem
                    # }
                ],
            },
            "operations": [
                {
                    "operationtype": 0,  # send message
                    "esc_period": 0,
                    "esc_step_from": 1,
                    "esc_step_to": 1,
                    "evaltype": 0,
                    "opmessage_usr": [{"userid": userid}],
                    "opmessage": {"default_msg": 1, "mediatypeid": mediatypeid},
                }
            ],
        },
        "auth": token,
        "id": 1,
    }
    resp = http_post(data=payload)
    print('create action', resp)


if __name__ == '__main__':
    action_ids = action_get()
    action_delete(action_ids)
    action_create()
