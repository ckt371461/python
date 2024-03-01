def pmul(a,b):
    c = [0] * (len(a)+len(b)-1)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i+j] += a[i]*b[j]
    return c

def pdiv(a,b):
    la, lb = len(a), len(b)
    r = a.copy()
    q = [0] * (la-lb+1)
    for i in range(la-lb+1):
        scale = r[i]/b[0]
        q[i] = scale
        di = la-1-i
        for j in range(lb):
            dj = lb-1-j
            r[la-di-dj] -= b[j]*scale
    return {'r': r[-lb+1:], 'q': q}

x = [3,3,2]
y = [1,1]

print('x=', x, 'y=', y)
print('pmul(x,y)=', pmul(x,y))
print('pdiv(x,y)=', pdiv(x,y))
    


    
     



    

