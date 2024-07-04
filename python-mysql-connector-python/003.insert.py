import mysql.connector

conn = mysql.connector.connect(
    host='8.4.4.4',
    port=13306,
    user='root',
    password='13243',
    database='atom_test_db',
)

cursor = conn.cursor()

# mysql 的占位符是 %s
cursor.execute("insert into user_1(id,name) values (%s,%s)", [6, 'atom2'])
conn.commit()

conn.close()
