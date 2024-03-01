from pymongo import MongoClient
conn=MongoClient()
db=conn.news
collection=db.nkust
find_cmd={'date':{'$gte':'2022-10-22'}}
# $gte 表示大於等於的意思
rows=collection.find(find_cmd)
if rows:
    for row in rows:
        print(row['title'])
else:
    print('找不到當天新聞')
