import math
class i:
    def __init__(self,a,b):
        self.a,self.b = a,b
    def add(self,c):
        return i(c.a+self.a,c.b+self.b)
    def less(self,c):
        return i(self.a-c.a,self.b-c.b)
    def mul(self,c):
        return i(self.a*c.a-self.b*c.b,self.a*c.b+self.b*c.a)
    def div(self,c):
        return i((self.a*c.a+self.b*c.b)/(c.a**2+c.b**2),(self.b*c.a-self.a*c.b)/(c.a**2+c.b**2))
    def exp(self):
        return i((math.e**self.a)*math.cos(self.b),(math.e**self.a)*math.sin(self.b))
    def ln(self):
        r =(self.a**2+self.b**2)**(1/2)
        s = math.acos(self.a/r)
        log_r = math.log(r)
        return i(log_r,s)
    def __str__(self):
        return f'{self.a}+{self.b}i'
    

c = i(1,2)
k=  i(2,3)
print (i.add(k,c))
print (k.mul(c))
print (k.div(c))
print (k.exp())
print (k.ln())
# print (i.add(k,c).b)
# print (i.less(k,c).a)
# print (i.less(k,c).b)