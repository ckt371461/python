import sqlite3
conn=sqlite3.connect('books.db')
cursor=conn.cursor()
sql1='SELECT title FROM books ORDER BY title ASC'
sql2='SELECT * FROM books ORDER BY year ASC'
for line in cursor.execute(sql1):
    print(line)
for line in cursor.execute(sql2):
    print(line)