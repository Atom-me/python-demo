import requests

# 直接在URL中携带参数
url = "https://www.baidu.com/s?wd=python"
# 构建请求头，伪装浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
# 发送get请求
response = requests.get(url, headers=headers)

with open('baidu.html', 'wb') as f:
    f.write(response.content)
