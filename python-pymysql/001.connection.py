import pymysql
from pymysql import Connection

con = None

try:
    # 创建数据库连接
    con = Connection(
        host='1.1.1.1',
        port=13306,
        user='root',
        password='D111.123',
    )

    print(type(con))
    print(con.get_host_info())
    print(con.get_server_info())
except pymysql.MySQLError as e:
    print("异常", e)
finally:
    if con:
        # 关闭连接
        con.close()
