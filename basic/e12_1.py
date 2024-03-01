import unicodedata
mystery='\U0001f984'
name=unicodedata.name(mystery)
print(f'name = {name} , code = {mystery}')
pop_bytes=mystery.encode('utf-8')
pop_string=pop_bytes.decode('utf-8')
print(mystery==pop_string)