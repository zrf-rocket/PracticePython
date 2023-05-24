from zabbix_api import username, password, url
import json
import datetime
import requests
from pyzabbix import ZabbixAPI

boturl = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=*****************"
headers = {'Content-Type': 'application/json;charset=utf-8'}


def msg(text):
    json_text = {
        "msgtype": "text",
        "text": {
            "content": text
        },
    }
    print(requests.post(boturl, json.dumps(json_text), headers=headers).content)


def alert_msg():
    # zabbix地址和登录信息
    ZABBIX_SERVER = url
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login(username, password)

    # 获取告警信息
    alert_list = zapi.trigger.get(
        output=[
            "triggerid",  # 触发器id
            "description",  # 触发器内容描述
            "priority",  # 触发器等级1-5  5最大 信息、警告、一般严重、严重、灾难
        ],
        filter={
            "value": 1  # 过滤，此处表示启动的触发器
        },
        sortfield="priority",  # 排序
        sortorder="DESC",  # 正排与倒排
        min_severity=2,  # 返回指定告警级别的告警，这里是大于等于告警
        skipDependent=1,  # 跳过依赖于其他问题中的触发器
        monitored=1,  # 属于受监控主机的已启用触发器，并仅包含已启用的项目
        active=1,  # 只返回属于受监控主机的启用的触发器（与上条意思差不多，至于什么区别，未测）
        expandDescription=1,  # 在触发器的名称中展开宏
        selectHosts=['name'],  # 在结果中返回关联的主机信息（意思就是显示出那台主机告警的）
        selectGroups=['name'],  # 在结果中返回关联的主机组信息（意思就是显示出那个主机组告警的）
        only_true=1  # 只返回最近处于问题状态的触发器
    )
    now_date = datetime.datetime.now()
    info = ''
    info += '当前存在告警：\n' + str(now_date)
    for i in alert_list:
        info += '\n\n名称:' + i['hosts'][0]['name'] + '\n告警内容：' + i['description']
    msg(info)


if '__main__' == __name__:
    alert_msg()