import requests

# 目标URL
url = "https://baidu.com"

# 发送get请求
response = requests.get(url)


# 常见的响应对象参数和方法
print(response.url)
# 响应状态码
print(response.status_code)
# 请求头
print(response.request.headers)
#  响应头
print(response.headers)

# 返回 RequestsCookieJar 对象
print(response.cookies)

# print(response.json())





