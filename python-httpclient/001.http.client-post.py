import http.client
import json

# 这里host不能写 http://localhost （http.client.HTTPConnection 的第一个参数应该是主机名（hostname），而不是完整的 URL。）
# 因为 http.client.HTTPConnection 默认使用 HTTP 协议，所以不需要在主机名中包含协议前缀。
conn = http.client.HTTPConnection('localhost', 8080)

headers = {'Content-type': 'application/json'}

params = {'lastName': 'Liu', 'firstName': 'Atom', "email": "sarming@126.com", "address": "beijing haidian"}
body = json.dumps(params)

conn.request('POST', '/create', body, headers)

response = conn.getresponse()
print(response.read().decode())
