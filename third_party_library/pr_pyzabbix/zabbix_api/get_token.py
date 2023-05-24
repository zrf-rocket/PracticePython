from zabbix_api import username, password
from http_request import http_post

def user_login():
    """
    用户登录，获取token
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {"user": username, "password": password},
        "id": 1,
        "auth": None,
    }
    resp = http_post(data=payload)
    token = resp.get("result")
    if not token:
        raise u"Zabbix账号密码不正确，请输入管理员账号密码"
    return token


if __name__ == '__main__':
    print(user_login())
