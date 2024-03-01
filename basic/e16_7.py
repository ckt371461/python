import redis
conn=redis.Redis()
conn.hset('test','count',1)
conn.hset('test','name','Fester Bestertester')
print(conn.hgetall('test'))
conn.hincrby('test','count',3)
print(conn.hgetall('test'))
