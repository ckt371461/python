'''
def min(a,b):
    if a > b: 
        return b
    elif a < b:
        return a
    else: return int((a+b)/2)        
'''

def min(a,b):
    if a > b: 
        return b
    else:
        return a

print('min(3,5)=', min(3,5))
print('min(8,2)=', min(8,2))
print('min(3,3)=', min(3,3))
