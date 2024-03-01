def df(f,h,x):
    return (f(x+h)-f(x))/h

def f(x):
    return x*x

x=2
z=0.00001
print (df(f,z,x))