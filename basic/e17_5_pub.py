import zmq
host='127.0.0.1'
port=6789
context=zmq.Context()
pub=context.socket(zmq.PUB)
pub.bind(f'tcp://{host}:{port}')
import time
time.sleep(1)
mammoth='''We have seen the Queen of cheese,
Laying quietly at your ease,
Gently fanned by evening breeze --
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial Show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees --
Or as the leaves upon the trees --
It did require to make thee please,
And stand unrivalled Queen of Cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great World's show at Paris.

Of the youth -- beware of these --
For some of them might rudely squeeze
And bite your cheek; then songs or glees
We could not sing o' Queen of Cheese.

We'rt thou suspended from baloon,
You'd cast a shade, even at noon;
Folks would think it was the moon
About to fall and crush them soon.'''
import re
'''mammoth_split=mammoth.split('')
for msg in mammoth_split:
    msg=msg.strip('\W')
    if msg
    msg_bytes=msg.encode('utf-8')
    pub.send(msg_bytes) 
    在這邊先要先處理訂閱者的分類，不能直接送出'''
pat1=r'\b[a,e,i,o,u,A,E,I,O,U]\w*\b'
vowels=re.findall(pat1,mammoth)
for vowel in vowels:
    vowel_bytes=vowel.encode('utf-8')
    pub.send_multipart([b'vowels',vowel_bytes])
    print([b'vowels',vowel_bytes])
pat2=r'\b\w{5}\b'
fives=re.findall(pat2,mammoth)
for five in fives:
    five_bytes=five.encode('utf-8')
    pub.send_multipart([b'five',five_bytes])
    print([b'five',five_bytes])