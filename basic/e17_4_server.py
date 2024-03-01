import redis,random,time
conn=redis.Redis()
chocolates=['dark chocolate','milk chocolate','white chocolate','nut chocolate','alcoholic chocolate','chocolate truffle']
while True:
    time.sleep(random.random())
    chocolate=random.choice(chocolates)
    conn.rpush('chocolate',chocolate)
    # rpush 從結尾插入, lpush從開頭插入
