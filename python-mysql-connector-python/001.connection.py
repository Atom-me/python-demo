"""
mysql-connector-python
是mysql官方的驱动

pip install mysql-connector-python

"""
import mysql.connector

conn = mysql.connector.connect(
    host='8.4.4.4',
    port=13306,
    user='root',
    password='13243',
    database='atom_test_db',
)

print(conn)
print(conn.get_server_info())
print(conn.get_server_version())
