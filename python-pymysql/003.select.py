"""
mysql 数据库模块同样可以使用游标的execute()方法执行DML语句
"""

import pymysql
from pymysql import Connection

con = None

try:
    # 创建数据库连接
    con = Connection(
        host='1.1.1.1',
        port=135306,
        user='root',
        password='werq.123',
        database='werq',
    )

    # 创建游标对象
    cursor = con.cursor()

    # 使用游标对象，执行SQL, 游标对象不用手动关闭，可以省略，因为关闭connection的时候会自动关闭cursor。
    cursor.execute("select * from tbl_user")

    # 获取查询结果
    result = cursor.fetchall()
    print(type(result), result)
    for row in result:
        print(type(row), row)

except pymysql.MySQLError as e:
    print("异常", e)
finally:
    if con:
        # 关闭连接
        con.close()
