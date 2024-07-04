import mysql.connector

conn = mysql.connector.connect(
    host='8.4.4.4',
    port=13306,
    user='root',
    password='13243',
    database='atom_test_db',
)

cursor = conn.cursor()

cursor.execute("create table user_1(id int auto_increment primary key, name varchar(255))")
conn.commit()

conn.close()
