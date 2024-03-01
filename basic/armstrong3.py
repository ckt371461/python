def armstrong(n): 
    s = []
    sum =0
    u = n
    while u >= 10:
        t = u % 10 
        s.append(t)
        u = int((u-t)/10)
    s.append(u) 
    for d in s:
        sum = d**len(str(n)) + sum
    # print(sum)
    '''
    if sum == n:
        return True
    else:
        return False 
    '''    
    return sum == n
print(armstrong(156))
print(armstrong(153))
