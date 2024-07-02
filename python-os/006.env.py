import os


"""
获取环境变量键的值（存在），否则返回默认值
os.getenv(key, default = None)

参数
key:表示环境变量名称的字符串
default (可选)：表示 key 不存在时默认值的字符串。如果省略，则默认设置为“无”。

"""


print(os.getenv("AUTH_TYPE"))

print(os.getenv("AUTH_TYPE", default="basic"))