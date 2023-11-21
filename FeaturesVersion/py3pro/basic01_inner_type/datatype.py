num1 = 12345
print(type(num1), type(0), type(-1))  # <class 'int'> <class 'int'> <class 'int'>


num2 = 12345.
num3 = 123.467
num4 = -123.467
print(type(num2))  # <class 'float'>
print(type(num3))  # <class 'float'>
print(type(num4))  # <class 'float'>


num5 = 3 + 5j
print(type(num5))  # <class 'complex'>


b1 = True
b2 = False
print(type(b1), type(b2))  # <class 'bool'> <class 'bool'>
# 其他类型转为bool类型
print(bool(123))  # True
print(bool(""))  # False
print(bool(None))  # False

l1 = False
l2 = True
print(l2 or l1)  # True
print(False and False)  # False


from FeaturesVersion import AGE, BLOG, WEIXIN_URL, AUTHOR

print(BLOG, WEIXIN_URL)  # 微信公众号：CTO Plus https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
print(type(BLOG), type(WEIXIN_URL))  # <class 'str'> <class 'str'>

s1 = 'a'
s2 = 'SteveRocket'
s3 = """微信公众号：CTO Plus
Author：SteveRocket"""
print(type(s1), type(s2), type(s3))  # <class 'str'> <class 'str'> <class 'str'>


li1 = [1, 2, 3, 4, 5]
li2 = [AGE, WEIXIN_URL, BLOG, {"user": AUTHOR}]
print(li1, li2)
print(type(li1), type(li2))  # <class 'list'> <class 'list'>


t1 = (1, 2, 3, 4, 5)
t2 = (AGE, WEIXIN_URL, BLOG, {"user": AUTHOR})
print(t1, t2) # (1, 2, 3, 4, 5) (28, 'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q', '微信公众号：CTO Plus', {'user': 'steverocket'})
print(type(t1), type(t2)) # <class 'tuple'> <class 'tuple'>

t3 = (11, 2, 11, 4, 11)
print(t3)  # (11, 2, 11, 4, 11)


set1 = {11, 22, 33}
# set2 = {AGE, AUTHOR, WEIXIN_URL, {'user':{"Author":AUTHOR, 'Age':AGE}}} # TypeError: unhashable type: 'dict'
# set2 = {AGE, AUTHOR, WEIXIN_URL, {}}  # TypeError: unhashable type: 'dict'
set2 = {AGE, AUTHOR, WEIXIN_URL}
print(set1, set2)  # {33, 11, 22} {'steverocket', 'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q', 28}
print(type(set1), type(set2))  # <class 'set'> <class 'set'>

set1 = {1, 2, 3}
set2 = {2, 3, 4}

# 集合求交集
print(set1 & set2)  # 输出：{2, 3}

# 集合求并集
print(set1 | set2)  # 输出：{1, 2, 3, 4}

# 集合求差集
print(set1 ^ set2)  # 输出：{1, 4}
print(set1 - set2)  # 输出：{1}
print(set2 - set1)  # 输出：{4}

d1 = {'name': AUTHOR, 'age': AGE, 'blog': BLOG}
d2 = {1: 'steverocket', 2: 'cramer', 3: 'python', 'user_info': d1}
print(d1, d2) # {'name': 'steverocket', 'age': 28, 'blog': '微信公众号：CTO Plus'} {1: 'steverocket', 2: 'cramer', 3: 'python', 'user_info': {'name': 'steverocket', 'age': 28, 'blog': '微信公众号：CTO Plus'}}
print(type(d1), type(d2)) # <class 'dict'> <class 'dict'>













"""
import json
from requests import post

data = {
    'customS1': None, 'customS2': None, 'aggregatedCount': 1, 'protocol': None,
    'collectorAddr': '192.168.1.160', 'customD3': None, 'customD2': None,
    'dName': None, 'dAddr': None,
    'customS3': None, 'result': None, 'devVendor': None, 'sAddr': None,
    'dPort': None, 'customS4': None, 'customD1': None, 'uid': 'abf774434fdd445360ebacda40dd8189',
    'category': None, 'occurTime': '2018-04-02 15:55:27.924523',
    'sName': None, 'devAddr': '192.168.1.30', 'devProduct': None,
    'devName': None, 'priority': 1, 'policy': None,
    'type': None, 'customD4': None, 'object': None, 'devCategory': 1, 'appProtocol': None,
    'collectType': 3, 'msg': {'PLC8': '0.12'}, 'intent': None,
    'receptTime': '2018-04-02 15:55:27.924', 'collectorName': 'djangeserver',
    'ID': None, 'resource': None, 'name': '收到采集指标', 'rawID': 61974, 'devType': None,
    'oriPriority': 5, 'action': None,
    'sPort': None, 'sysType': 2
}

# post(url= 'http://192.168.1.122:8122/normalization/sendLog',json=data)
# print( data["names"])


# for name,age in {"name":"python","age":12}:
#     print name,age


# patch = "KB2718695,KB2718695,KB2670838,KB2479943,KB2491683,KB2506014,KB2506212,KB2509553,KB2511455,KB2533623,KB2534111,KB2536275,KB2536276,KB2544893,KB2552343,KB2560656,KB2564958,KB2570947,KB2579686,KB2584146,KB2585542,KB2604115,KB2619339,KB2620704,KB2620712,KB2621440,KB2631813,KB2639308,KB2653956,KB2654428,KB2655992,KB2656356,KB2659262,KB2667402,KB2676562,KB2685811,KB2685939,KB2690533,KB2698365,KB2705219,KB2706045,KB2712808,KB2727528,KB2729094,KB2729452,KB2731771,KB2736422,KB2742599,KB2743555,KB2757638,KB2758857,KB2770660,KB2786081,KB2789645,KB2803821,KB2807986,KB2813430,KB2839894,KB2840149,KB2840631,KB2847927,KB2855844,KB2861698,KB2862152,KB2862330,KB2862335,KB2862966,KB2862973,KB2864058,KB2864202,KB2868038,KB2868626,KB2868725,KB2871997,KB2872339,KB2876331,KB2884256,KB2892074,KB2893294,KB2894844,KB2900986,KB2911501,KB2912390,KB2931356,KB2937610,KB2943357,KB2957189,KB2957503,KB2968294,KB2972100,KB2972211,KB2973112,KB2973201,KB2973351,KB2977292,KB2978120,KB2978668,KB2978742,KB2980245,KB2984972,KB2990941,KB2991963,KB2992611,KB2993651,KB3000483,KB3003743,KB3004361,KB3004375,KB3005607,KB3010788,KB3011780,KB3012176,KB3019978,KB3021674,KB3022777,KB3023215,KB3023607,KB3030377,KB3033889,KB3035126,KB3035131,KB3035132,KB3037574,KB3042553,KB3045171,KB3045685,KB3045999,KB3046017,KB3046269,KB3055642,KB3057154,KB3059317,KB3060716,KB3061518,KB3063858,KB3067903,KB3071756,KB3072305,KB3072630,KB3072633,KB3074543,KB3075220,KB3076895,KB3076949,KB3078071,KB3078601,KB3080446,KB3081320,KB3083992,KB3084135,KB3086255,KB3087039,KB3087873,KB3092601,KB3093513,KB3097966,KB3097989,KB3101722,KB3101746,KB3108371,KB3108381,KB3108664,KB3108670,KB3109094,KB3109103,KB3109560,KB3110329,KB3115858,KB3121461,KB3121918,KB3122648,KB3124275,KB3124280,KB3126587,KB3126593,KB3127220,KB3135983,KB3135988,KB3138612,KB3138910,KB3138962,KB3139398,KB3139914,KB3139940,KB3142024,KB3142042,KB3146963,KB3149090,KB3150220,KB3155178,KB3156016,KB3156017,KB3156019,KB3159398,KB3161561,KB3161664,KB3161949,KB3161958,KB3163245,KB3164033,KB3164035,KB3168965,KB3170455,KB3177467,KB4048960,KB976902,KB4054518"
# print patch.count("KB")

patch = "KB3134228,KB3079904,KB3077657,KB3000061,KB2829361,KB2850851,KB2707511,KB2124261,KB970483,KB3124263,KB2360937,KB2478960,KB2507938,KB2566454,KB2646524,KB2645640,KB2641653,KB944653,KB952004,KB971657,KB2393802,KB942831,KB2503665,KB2592799,KB956572,KB977165,KB3143141,KB2271195,KB4012598,KB4012212"
print(patch.count("KB"))




d = {"1": "asd"}
print(d.get("2", "没找到"))






s = "d4cbd0d0cfb5cdb33a20c6f4b6af2e2e2e"

s2 = "\\x4E2D;\\x6587;"
print(s2.encode('iso-8859-1').decode('gbk'))
# print s2.encode("gbk").decode("utf-8")
"""
