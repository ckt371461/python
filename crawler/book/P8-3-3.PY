from pymongo import MongoClient
conn=MongoClient()
db=conn.news
collection=db.nkust
find_cmd={'date':{'$in':['2022-10-22','2022-10-28']}}
# $in 表示包含的意思
rows=collection.find(find_cmd)
if rows:
    for row in rows:
        print(row['title'])
else:
    print('找不到當天新聞')
