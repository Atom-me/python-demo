import requests

# 目标URL
url = "https://baidu.com"

# 发送get请求
response = requests.get(url)

print(response.encoding)
print(response.text)
print("================================================================================================")

# 打印响应内容
# response.encoding = 'utf-8'
# print(response.text)
# print(response.encoding)


# response.content 返回 bytes类型，可以使用decode方法解码
# print(response.content)

# 通过 对 response.content 进行decode，来解决中文乱码问题
# response.content.decode() 默认utf-8
# response.content.decode('GBK) 指定编码集

print(response.content.decode())


