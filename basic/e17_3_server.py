from xmlrpc.server import SimpleXMLRPCServer
server=SimpleXMLRPCServer(('127.0.0.1',6789))
def now(input):
    if input == 'time':
        from datetime import datetime
        now_object=datetime.now()
        now=now_object.isoformat()
        return now
server.register_function(now,'now')
server.serve_forever()