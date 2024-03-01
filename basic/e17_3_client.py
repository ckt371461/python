from xmlrpc import client
proxy=client.ServerProxy('http://127.0.0.1:6789/')
result=proxy.now('time')
print(result)
