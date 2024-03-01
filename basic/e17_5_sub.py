import zmq
host='127.0.0.1'
port=6789
context=zmq.Context()
sub=context.socket(zmq.SUB)
sub.connect(f'tcp://{host}:{port}')
topics=[b'vowels',b'five']
for topic in topics:
    sub.setsockopt(zmq.SUBSCRIBE,topic)
while True:
    title_bytes,data_bytes=sub.recv_multipart()
    title=title_bytes.decode('utf-8')
    data=data_bytes.decode('utf-8')
    print(f'Title: {title}, data: {data}')