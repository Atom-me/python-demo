"""
pymysql 对操作mysql ddl 提供了很好的支持。
连接mysql数据库后，可以使用游标，cursor()方法创建一个游标对象，游标对象用于执行mysql语句并返回结果
"""

import pymysql
from pymysql import Connection

con = None

try:
    # 创建数据库连接
    con = Connection(
        host='8.5.5.5',
        port=14306,
        user='root',
        password='232.123',
        database='atom_test_db',
    )

    # 创建游标对象
    cursor = con.cursor()

    # 定义DDL语句
    sql = """
    create table if not exists users2 (
    `id` int not null auto_increment,
    `name` varchar(20) default null,
    `age` int default null,
    primary key (`id`)
    ) engine=InnoDB default charset=utf8;
    """

    # 选择要操作的数据库， 也可以在connection上面直接配置DB
    # con.select_db("atom_test_db")

    # 使用游标对象，执行SQL, 游标对象不用手动关闭，可以省略，因为关闭connection的时候会自动关闭cursor。
    cursor.execute(sql)

except pymysql.MySQLError as e:
    print("异常", e)
finally:
    if con:
        # 关闭连接
        con.close()
