import binascii,struct
bytes='47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'
gif=binascii.unhexlify(bytes)
print(gif)
width,height=struct.unpack('<HH',gif[6:10])
print(f'width = {width} , height = {height}')