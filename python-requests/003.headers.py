import requests

# 目标URL
url = "https://baidu.com"

# 发送get请求
response = requests.get(url)
print(len(response.content.decode()))
print(response.content.decode())

# 构建请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
# 发送带请求头的请求
response2 = requests.get(url, headers=headers)
print(response2.content.decode())
print(len(response2.content.decode()))
