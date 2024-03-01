
def bigest (a,b,c):
    t = 0
    if a > b:
        t = a
    else: t = b
    if t > c:
        return t
    else: 
        return c            

print('bigest(3,1,2)=', bigest(3,1,2))      
print('bigest(9,15,22)=', bigest(9,15,22))      
print('bigest(8,25,1)=', bigest(8,25,1))      