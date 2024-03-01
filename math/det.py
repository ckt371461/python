import numpy as np
import random 
import scipy.linalg as la

a = np.random.rand(2,2)
b = np.random.rand(2,2)
print("a=",a)
print("b=",b)
print("det(a)=",np.linalg.det(a))
print("det(b)=",np.linalg.det(b))
def add(k,p):
    s=p.copy()
    s[[0,1]]+=s[[1,0]]*k 
    return s
def exchange_column(p):
    s=p.copy()
    s[[0,1]]=s[[1,0]]
    return s
def exchange_row(p):
    s=p.copy()
    s[:,[0,1]]=s[:,[1,0]]
    return s
def scale(k,p):
    s=p.copy()
    s[:,[0]]=s[:,[0]]*k
    print (s)
    return s

def lu(p):
    s=p.copy()
    return la.lu(s)

print(np.isclose(np.linalg.det(np.dot(a,b)),np.linalg.det(a)*np.linalg.det(b)))
p,l,u = lu(a)
print("det(u)=",np.linalg.det(u))
print("det(add(a))=",np.linalg.det(add(2,a)))
print ("det(exchangen(a))=",np.linalg.det(exchange_column(a)))
print("det(scale(a))=",np.linalg.det(scale(2,a)))

