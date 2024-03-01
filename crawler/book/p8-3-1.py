from pymongo import MongoClient
conn=MongoClient()
db=conn.news
collection=db.nkust
rows=collection.find({})#大括號表示不設任何條件，因此會找出全部資料
for row in rows:
    print(row)
    print('----------------------')