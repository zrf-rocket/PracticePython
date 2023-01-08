# -*- encoding:utf-8 -*-
import json

__AUTHOR__ = "zhouruifu"
__TIME__ = "2018/09/15"
__VERSION__ = 1.0

"""
模块docstring
# 标注：当前插件需要安装第三方依赖包：pip install 包名
# 注意事项：开发规范请参照开发对接文档
# 当前脚本为插件模板，每个接口输出结果均为正常的结果，异常的结果由编写插件人员按照规范文档自行处理
"""


class CodeDocstring(object):
    """
    代码docstring风格演示
    """
    def __init__(self):
        pass

    def get_access_info(self, ip, network_card_position = None, cpu_position = None, **kwargs):
        """
        获取设备访问信息的接口
        :param ip: str,设备ip
        :param network_card_position: str，网卡号，值可为空
        :param cpu_position: str,CPU号，值可为空
        :param kwargs: dict，可变参数
        :return: json，接口输出结果
        """
        pass