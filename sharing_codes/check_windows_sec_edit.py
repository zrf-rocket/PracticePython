# -*- encoding:utf-8 -*-

__AUTHOR__ = "zhouruifu"
__TIME__ = "2018/09/15"
__VERSION__ = 1.0

import codecs
# from show_data import show_json_datas


class ParserSecFileRes(object):
    def __init__(self):
        """
        一系列的初始化操作
        """
        self.secedit_items = {}
        self.export_sec_res()
        self.parser_sid = {
            "*S-1-1-0": "Everyone",
            "*S-1-5-6": "SERVICES",
            "*S-1-5-19": "LOCAL SERVICE",
            "*S-1-5-20": "NETWORK SERVICE",
            "*S-1-5-32-544": "Administrators"
        }

    def export_sec_res(self):
        try:
            # 读文件使用with
            with codecs.open("sec.ini", "r", "utf-16") as sec_file:
                for line in sec_file:
                    if "=" in line:
                        split_res = line.encode("utf-8").replace("\n", "").split("=")
                        self.secedit_items.setdefault(split_res[0].rstrip(), split_res[1].lstrip().replace("\r", ""))
        except IOError, e:
            pass

    def seremote_shutdown_privilege(self):
        # 获取字典的值，推荐使用get
        # self.secedit_items["SeRemoteShutdownPrivileges"] # key不存在会抛KeyError异常
        seremote_shutdown_privilege = self.secedit_items.get("SeRemoteShutdownPrivilege", None) # 不存在key 默认是None

        if not seremote_shutdown_privilege:
            is_comp = "未知"
            reason = "请以SYSTEM用户运行核查。"
        else:
            if seremote_shutdown_privilege == "*S-1-5-32-544":
                is_comp = "合规"
                reason = "从远端系统强制关机已仅指派给Administrators"
            else:
                is_comp = "不合规"
                reason = "从远端系统强制关机不是仅指派给Administrators"
            seremote_shutdown_privilege = self.parser_sid.get(seremote_shutdown_privilege, seremote_shutdown_privilege) # 不存在，则使用默认原始字段代替
        results = {"event_id": 1020, "is_comp": is_comp, "verification": "核查从远端系统强制关机仅指派给Administrators", "category": "登录与认证授权", "resource": seremote_shutdown_privilege, "reason": reason, "hazard_level": 2}
        print results
        # show_json_datas(results)

def main():
    psfr = ParserSecFileRes()
    psfr.seremote_shutdown_privilege()
    raw_input()


if __name__ == '__main__':
    main()
