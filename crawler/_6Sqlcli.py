import sqlite3

db = sqlite3.connect('stockPrice.db1')
cursor = db.cursor()
while True:
    print('sql:', end='')
    cmd = input()
    if cmd == 'exit': break
    cursor.execute(cmd)
    rows = cursor.fetchall()
    '''
    查詢回傳的資料需要以 cursor 物件的兩個方法取得：
    
    fetchall()：取出全部資料
    cursor.fetchall()
    
    fetchone()：取出第一筆資料
    cursor.fetchone()
'''
for row in rows:
    print(row)
db.close()
