import socket,datetime
server_address=('localhost',6789)
max_size=4096
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(server_address)
data,client=server.recvfrom(max_size)
if data == b'time':
    now=datetime.datetime.now().isoformat()
    now_bytes=now.encode('utf-8')
    server.sendto(now_bytes,client)
server.close()