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
        port=333,
        user='root',
        password='23eq.123',
        database='atom_test_db',
        autocommit=True
    )

    # 创建游标对象
    cursor = con.cursor()

    # 使用游标对象，执行SQL, 游标对象不用手动关闭，可以省略，因为关闭connection的时候会自动关闭cursor。
    cursor.execute("insert into users (name, age) values ('atom', 44)")

    # 可以设置自动提交
    # con.commit()

    # 可以直接获取插入之后的数据的主键ID
    print(con.insert_id())


except pymysql.MySQLError as e:
    print("异常", e)
finally:
    if con:
        # 关闭连接
        con.close()
