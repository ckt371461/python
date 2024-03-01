import zmq,datetime
host='127.0.0.1'
port=6789
context=zmq.Context()
server=context.socket(zmq.REP)
server.bind(f'tcp://{host}:{port}')
while True:
    request_byte=server.recv()
    if request_byte==b'time':
        now=datetime.datetime.now()
        now_bytes=now.isoformat().encode('utf-8')
        server.send(now_bytes)