import http.client

conn = http.client.HTTPConnection('localhost', 8080)

# path variable
user_id = 1
url = f'/user/{user_id}'

conn.request('GET', url)

response = conn.getresponse()

if response.status == 200:
    data = response.read().decode('utf-8')
    print(data)
else:
    print('请求失败:', response.status)

conn.close()
