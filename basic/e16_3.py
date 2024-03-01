import sqlite3
'''CREAT DATABASE books.db
USE book.db
CREAT TABLE books'''
conn=sqlite3.connect('books.db')
cursors=conn.cursor()
cursors.execute('CREATE TABLE books (title TEXT,author TEXT,year INT)')
conn.commit()