from pymongo import MongoClient
conn=MongoClient()
db=conn.news
collection=db.nkust
find_cmd={'title':{'$regex':"高科大"}}
# $regex 表示設定的搜尋字串
rows=collection.find(find_cmd)
if rows:
    for row in rows:
        print(row['title'])
else:
    print('找不到當天新聞')
