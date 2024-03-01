import sqlite3
db=sqlite3.connect("headlines.db")
#tno 是用來方便日後編輯，它會自動重1開始增加，且不會重複
sql="""
CREATE TABLE IF NOT EXISTS titles(
    tno INTEGER PRIMARY KEY,
    title TEXT NOT NULL UNIQUE,
    link TEXT
)
"""
db.execute(sql)
cursor=db.cursor()
for i in range(1,6):
    sql="insert into titles (title,link) values(?,?)"
    #後方的兩個問號代表值會在execute()執行指令的時候再提供
    cursor.execute(sql,('第{}筆標題'.format(i),'第{}個連結'.format(i)))
db.commit()
#connection物件負責資料庫級別的操作，cursor物件負責資料表級別的操作，row則是負責記錄層級的操作 