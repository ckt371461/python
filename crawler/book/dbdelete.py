import sqlite3
db=sqlite3.connect('headlines.db')
cur=db.cursor()
sql="delete from titles where link !='' "
cur.execute(sql)
db.commit()
db.close()
print('Done')