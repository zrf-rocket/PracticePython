import json
from zabbix_api import url

# python3 compatibility
try:
    import urllib2 as request
except Exception:
    from urllib import request

def force_bytes(s, encoding="utf-8", strings_only=False, errors="strict"):
    if isinstance(s, bytes):
        if encoding == "utf-8":
            return s
        else:
            return s.decode("utf-8", errors).encode(encoding, errors)
    return s.encode(encoding, errors)

def http_post(data, resp_fmt="json"):
    """
    POST方法封装
    data is dict or string
    """
    if isinstance(data, dict):
        data = json.dumps(data)
    data = force_bytes(data)

    req = request.Request(url, data=data, headers={"Content-Type": "application/json"})
    resp = request.urlopen(req, timeout=5).read()
    if resp_fmt == "json":
        resp = json.loads(resp)
    return resp
