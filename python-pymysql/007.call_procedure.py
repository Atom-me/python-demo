"""
调用存储过程


DELIMITER //
CREATE PROCEDURE test_add(m int, n int, out result int)
BEGIN
set result=m+n;
END;
//

delimiter ;


 测试：
set @s = 0;
call test_add(1,3,@s);
select @s;

"""

import pymysql
from pymysql import Connection

con = None

try:
    # 创建数据库连接
    con = Connection(
        host='8.8.8.8',
        port=333,
        user='root',
        password='2312312323',
        database='atom_test_db',
        autocommit=True
    )

    # 创建游标对象
    cursor = con.cursor()

    # 使用游标对象，调用存储过程
    cursor.execute("call test_add(1,3,@s);")
    cursor.execute("select @s;")

    result = cursor.fetchone()
    print(result[0])

except pymysql.MySQLError as e:
    print("异常", e)
finally:
    if con:
        # 关闭连接
        con.close()
