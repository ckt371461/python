import sqlalchemy as sa
conn=sa.create_engine('sqlite:///books.db')
for row in conn.execute('SELECT title FROM books ORDER BY title ASC'):
    print(row)
