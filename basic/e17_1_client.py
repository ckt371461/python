import socket
server_address=('127.0.0.1',6789)
max_size=4096
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(b'time',server_address)
data,server=client.recvfrom(max_size)
print(data)
client.close()
