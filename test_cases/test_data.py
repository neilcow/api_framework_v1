
# json数据必须要使用双引号，字典单引号 双引号都可以
# json里面用的是null，字典里用的是None
# 字符串转json的用法
import json

data = '{"login_name":"test", "pwd":null}'
# json字符串转成 字典
dict_data = json.loads(data, strict=False)
print(dict_data)
# {'login_name': 'test', 'pwd': None}
# 字典转成 json字符串
data_dict = {"name": "test1", "pwd": None}
data_json = json.dumps(data_dict)
print(data_json)
# {"name": "test1", "pwd": null}