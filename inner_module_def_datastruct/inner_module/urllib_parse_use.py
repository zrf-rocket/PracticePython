# https://blog.csdn.net/zhouruifu2015/article/details/50836516
from inner_module_def_datastruct import WEIXIN_URL
from urllib.parse import urljoin, urlparse, urlencode, urlsplit, urldefrag, urlunparse, urlunsplit

# 基础URL
base_url = "https://mp.weixin.qq.com"
# 相对URL
relative_url = "/s/0yqGBPbOI6QxHqK17WxU8Q"
# 拼接URL
full_url = urljoin(base_url, relative_url)
print(full_url)
print(WEIXIN_URL)

# 查询参数
params = {'id': 1, 'name': 'steverocket', 'age': 25}

# 拼接查询参数
query_string = urlencode(params)
print(query_string)  # id=1&name=steverocket&age=25

# 拼接URL
full_url = full_url + "?" + query_string
print(full_url)  # https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q?id=1&name=steverocket&age=25

# TODO 无法通过urljoin来拼接查询参数
# full_url2 = urljoin(full_url, query_string)
# print(full_url2)  # https://mp.weixin.qq.com/s/id=1&name=steverocket&age=25


url = 'http://www.example.com/path/page.html?query=abc#header'
parsed = urlparse(url)
print(parsed.scheme)  # http
print(parsed.netloc)  # www.example.com
print(parsed.path)    # /path/page.html
print(parsed.params)  #
print(parsed.query)   # query=abc
print(parsed.fragment)  # header


url = 'http://www.example.com/path/page.html?query=abc#header'
split = urlsplit(url)
print(split.scheme)    # http
print(split.netloc)    # www.example.com
print(split.path)      # /path/page.html
print(split.query)     # query=abc
print(split.fragment)  # header



url = 'http://www.example.com/path/page.html?query=abc#header'
split = urlsplit(url)
print(split.scheme)    # http
print(split.netloc)    # www.example.com
print(split.path)      # /path/page.html
print(split.query)     # query=abc
print(split.fragment)  # header
print(split)  # SplitResult(scheme='http', netloc='www.example.com', path='/path/page.html', query='query=abc', fragment='header')



url = 'http://www.example.com/path/page.html?query=abc#header'
url_without_fragment, fragment = urldefrag(url)
print(url_without_fragment)  # http://www.example.com/path/page.html?query=abc
print(fragment)             # header


url_parts = ('http', 'www.example.com', '/path/page.html', '', 'query=abc', 'header')
full_url = urlunparse(url_parts)
print(full_url)  # http://www.example.com/path/page.html?query=abc#header



url_parts = ('http', 'www.example.com', '/path/page.html', 'query=abc', 'header')
full_url = urlunsplit(url_parts)
print(full_url)  # http://www.example.com/path/page.html?query=abc#header



URL = "http://127.0.0.1/version"
dicts = {'platform': 'windows_64bit', 'object': 'agent', 'version': '20160216'}
os_type = {"os_type": "win_xp"}

def parse_url(data:dict):
    item = data.items()
    urls = "?"
    for i in item:
        (key, value) = i
        temp_str = key + "=" + value
        urls = urls + temp_str + "&"
    urls = urls[:len(urls) - 1]
    return urls

print(URL + parse_url(dicts))
print(URL + parse_url(os_type))

# 输出结果：
# http://127.0.0.1/version?platform=windows_64bit&object=agent&version=20160216
# http://127.0.0.1/version?os_type=win_xp
