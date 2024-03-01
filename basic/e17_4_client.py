import time,redis,datetime
conn=redis.Redis()

while True:
    time.sleep(0.5)
    # lpop從開頭取出，rpop從結尾取出
    #Redis Rpop 命令用于移除列表的最后一个元素，返回值为移除的元素。
    # brpop是rpop的阻塞版本。Redis Brpop 命令移出并获取列表的最后一个元素， 
    # 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止
    chocolate=conn.blpop('chocolate',timeout=10)#裡面没有元素会阻塞10秒
    #Redis Llen 命令用于返回列表的长度。 如果列表key 不存在，则key 被解释为一个空列表，返回0 。 如果key 不是列表类型，返回一个错误。
    remain=conn.llen('chocolate')
    #chocolate 是一個元祖(b'chocolate', b'milk chocolate')所以用chocolate[1]取出巧克力總類就好
    if chocolate:
        print(f'Lusy got a {chocolate[1]} at {datetime.datetime.now()}, only {remain} left.')