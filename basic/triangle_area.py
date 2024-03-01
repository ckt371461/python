# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c))
import cmath

def triangle_area(a,b,c):
    s = (a+b+c)/2
    area2 = (s*(s-a)*(s-b)*(s-c))
    a = area2**(1/2)
    #return cmath.sqrt(area2)
    return(a)

print('triangle_area(3,4,5)=', triangle_area(3,4,5))
