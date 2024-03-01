def div(a,b):
    if len(a)>=len(b):
        r = a.copy()
        q = [0]*(len(a)-len(b)+1)
        for x in range(len(a)-len(b)+1):
            q[x] = r[x]/b[0]
            for y in range(len(b)):
                r[y+x] -= q[x]*b[y]
        return{"q": q,"r" : r[len(a)-len(b)+1:]}
    elif len(a)<len(b):
        return a

def common_factor(a,b):
    while b != [0]:
        print('a=', a,'b=', b)
        r = div(a,b)["r"]
        # t = a
        a = b
        b = r
    return a
print('common_factor=', common_factor([1,2,1],[1,1]))
print(div([1,2,5,5],[2,4,3]))
print('common_factor=', common_factor([1,2,5,5],[2,4,3]))
