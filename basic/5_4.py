letter='''Dear {salutation} {name},
Thank you for tour letter. We are sorry that our {product} {verbed} in your {room},especially near any {animal}.
Send us your recipt and {amount} for shipping and handling.
We will send you another {product} thay, in our tests,is {precent}% less likely to have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}
'''

print(letter.format(salutation='1',
product=3,
name='ABC',
room=6,
verbed=2,
amount=32,
animal=231,
precent=5,
spokesman=32,
job_title='eaw'))



#要用字典的話要改寫格式，而{0}是指format()的第一個引數
letter_d='''Dear {0[salutation]} {0[name]},
Thank you for tour letter. We are sorry that our {0[product]} {0[verbed]} in your {0[room]},especially near any {0[animal]}.
Send us your recipt and {0[amount]} for shipping and handling.
We will send you another {0[product]} thay, in our tests,is {0[precent]}% less likely to have {0[verbed]}.
Thank you for your support.
Sincerely,
{0[spokesman]}
{0[job_title]}
'''
letter_dictionary={
'salutation':'1',
'product':3,
'name':'ABC',
'room':6,
'verbed':2,
'amount':32,
'animal':231,
'precent':5,
'spokesman':32,
'job_title':'eaw'
}
print(letter_d.format(letter_dictionary))