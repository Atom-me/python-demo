"""
json 模块提供了一种很简单的方式来编码和解码JSON数据。 其中两个主要的函数是 json.dumps() 和 json.loads() ， 要比其他序列化函数库如pickle的接口少得多。

如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。例如：

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)

"""
import json

# 解析json数据
with open('./config.json', 'r') as f:
    config_json = json.load(f)

# 获取"name": "sso"的数据
sso_data = None
for profile in config_json['profiles']:
    if profile["name"] == "sso":
        sso_data = profile
        break

# 获取 "stsToken" 数据
sts_token = None
if sso_data is not None:
    sso_auth = sso_data.get("ssoAuth")
    if sso_auth is not None:
        sts_token = sso_auth.get("stsToken")

# 打印获取到的 "stsToken" 数据
# if sts_token is not None:
#     print(sts_token)
# else:
#     print("未找到'stsToken'的数据")

accessKeyId = sts_token.get("accessKeyId")
secretAccessKey = sts_token.get("secretAccessKey")
securityToken = sts_token.get("securityToken")

print("accessKeyId: ", accessKeyId)
print("secretAccessKey: ", secretAccessKey)
print("securityToken: ", securityToken)
