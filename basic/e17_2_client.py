import zmq
host='127.0.0.1'
port=6789
context=zmq.Context()
client=context.socket(zmq.REQ)
client.connect(f'tcp://{host}:{port}')
client.send(b'time')
reply_bytes=client.recv()
reply=reply_bytes.decode('utf-8')
print(reply)
