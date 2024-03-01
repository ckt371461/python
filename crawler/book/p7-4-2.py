import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='books',
    user='root',
    password='#Cktim082371461'
)
if conn.is_connected():
    print('Successful')
    conn.close()
else:
    print('Fail to connect')
    conn.close()