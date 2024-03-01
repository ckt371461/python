import sqlite3,csv
with open('books2.csv','r',encoding='utf-8') as outfile:
    conn=sqlite3.connect('books.db')
    cursor=conn.cursor()
    books=csv.DictReader(outfile)
    ins='INSERT INTO books (title,author,year) VALUES(?,?,?)'
    for book in books:
        cursor.execute(ins,(book['title'],book['author'],book['year']))
    conn.commit()
    #記得要commit


