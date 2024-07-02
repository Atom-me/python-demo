import base64

"""
Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。

语法
strip()方法语法：

str.strip([chars]);

"""

"""拼接 http basic认证的header"""

# 定义了两个文件路径变量， 文件包含了用于认证的凭据信息
access_token_filename = "/Users/atom/access/token"
access_user_filename = "/Users/atom/access/username"

# 打开文件并读取文件内容来获取凭据信息。使用 open() 函数打开文件，
# 并指定 "r" 参数以表示读取模式。然后使用 .read() 方法读取文件内容，
# 并使用 .strip() 方法去除可能存在的额外空格或换行符，以得到凭据信息
token = open(access_token_filename, "r").read().strip()
username = open(access_user_filename, "r").read().strip()

# 将用户名和令牌信息组合成一个认证凭据字符串 auth_credentials
auth_credentials = f"{username}:{token}"


# 使用 base64 模块的 b64encode() 函数对凭据进行编码
# 首先，使用 .encode() 方法将凭据字符串转换为字节流，
# 然后使用 base64.b64encode() 对字节流进行编码。
# 编码后的结果是一个字节字符串，需要使用 .decode('ascii') 方法将其转换为可读的 ASCII 字符串。
encoded_credentials = base64.b64encode(auth_credentials.encode()).decode('ascii')

authHeader = f'Basic {encoded_credentials}'

print(authHeader)
