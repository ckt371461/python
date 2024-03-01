def 配方法(a,b,c):
    c = c/a
    b = b/a
    a = a/a
    d = (b/2)**2
    e = d - c
    #(x+(b/2))**2 = e
    return [-b/2 + e**0.5,-b/2 - e**0.5]
print(配方法(1,2,-3))

