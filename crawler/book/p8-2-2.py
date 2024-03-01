from pymongo import MongoClient
conn=MongoClient()
db=conn.news
collection=db.nkust
collection.insert_one({'date':'2020-02-13','title':'測試標題','content':'測試文字'})