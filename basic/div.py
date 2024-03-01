def div(a,b):
    if len(a)>=len(b):
        r = a 
        q = [0]*(len(a)-len(b)+1)
        for x in range(len(a)-len(b)+1):
            q[x] = r[x]/b[0]
            for y in range(len(b)):
                r[y+x] -= q[x]*b[y]
        return{"q": q,"r" : r[len(a)-len(b)+1:]}
    elif len(a)<len(b):
        return a

print (div([1,3,-5],[1,5]))
print (div([1,3,-5],[1,6,5]))
print (div([1,3,-5],[1,2,8,7]))