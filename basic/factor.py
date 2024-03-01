def factor(a):
    k=[]
    for s in range(2,a+1):
        while a % s ==0:
            k.append(s)
            a = a/s
    return k
print(factor(55))
print(factor(9999))

                                                                                                         