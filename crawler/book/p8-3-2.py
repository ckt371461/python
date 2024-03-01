from pymongo import MongoClient
conn=MongoClient()
db=conn.news
collection=db.nkust
rows=collection.find({'date':'2022-10-28'})

if rows:
    for row in rows:
        print(row['title'])
else:
    print('找不到當天新聞')
