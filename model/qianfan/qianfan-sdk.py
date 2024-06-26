
import os
import qianfan

#通过环境变量初始化认证信息
# 方式一：【推荐】使用安全认证AK/SK鉴权
# 替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
os.environ["QIANFAN_ACCESS_KEY"] = "your_iam_ak"
os.environ["QIANFAN_SECRET_KEY"] = "your_iam_sk"

# 方式二：【不推荐】使用应用AK/SK鉴权
# 替换下列示例中参数，将应用API_Key、应用Secret key值替换为真实值
#os.environ["QIANFAN_AK"] = "应用API_Key"
#os.environ["QIANFAN_SK"] = "应用Secret_Key"

chat_comp = qianfan.ChatCompletion()

# 指定特定模型
resp = chat_comp.do(model="ERNIE-3.5-8K", messages=[{
    "role": "user",
    "content": "你好"
}])

print(resp["body"])
