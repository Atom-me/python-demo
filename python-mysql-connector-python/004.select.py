import mysql.connector

conn = mysql.connector.connect(
    host='8.4.4.4',
    port=13306,
    user='root',
    password='13243',
    database='atom_test_db',
)

cursor = conn.cursor()

cursor.execute("select * from user_1 ")
values = cursor.fetchall()
print(values)

for value in values:
    print(value)

conn.close()
