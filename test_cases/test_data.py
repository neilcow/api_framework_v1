# json数据必须要使用双引号
# 字符串转json的用法
import json

data = "{"login_name":"test", "pwd":"123"}"
dict_data = json.loads(data)
print(dict_data)
# json转字符串的用法
