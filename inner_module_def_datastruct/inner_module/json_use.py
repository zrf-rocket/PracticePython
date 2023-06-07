# https://blog.csdn.net/zhouruifu2015/article/details/51429913
from inner_datastruct import WEIXIN_URL
import json

# 定义一个JSON字符串
json_str = '{"name": "steverocket", "age": 25, "city": "New York"}'

# 将JSON字符串转换为Python对象
data = json.loads(json_str)

# 打印Python对象
print(data)  # {'name': 'steverocket', 'age': 25, 'city': 'New York'}

# 访问Python对象的属性
print(data['name'])  # steverocket
print(data['age'])  # 25
print(data['city'])  # New York

import json

# 定义一个Python字典
data = {
    "name": "steverocket02",
    "age": 26,
    "city": "New York"
}

# 将Python字典转换为JSON格式的字符串，并格式化输出
json_str = json.dumps(data, indent=4)

# 打印JSON格式的字符串
print(json_str)
# 输出
# {
#     "name": "steverocket02",
#     "age": 26,
#     "city": "New York"
# }



import json, time

infos = {"_id": "description", "name": "python", "filename": "中文", "os": ["abcd", "hello", "www"], "blog": WEIXIN_URL}
infos["time"] = time.time()  # 动态修改json文件内容

# 生成json文件
def write_json_file(file_name, infos):
    with open(file_name, "w") as jsonf:
        jsonf.write(json.dumps(infos))

def read_json_file(file_name):
    # 读取json文件的内容
    with open(file_name, 'r') as jsonf:
        file_info = json.load(jsonf)
        print(file_info, type(file_info))

        filename = file_info["filename"]
        print(filename)

        infos = json.dumps(file_info, sort_keys=True, indent=4)
        print(infos, type(infos))

if __name__ == '__main__':
    file_name = "desc.json"
    write_json_file(file_name, infos)
    read_json_file(file_name)