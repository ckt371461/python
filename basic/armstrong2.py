def armstrong(n,k): # 檢查 n 是否為 k 階的阿姆斯壯數
    s = []
    sum =0
    u = n
    while u >= 10:
        t = u % 10 
        s.append(t)
        u = int((u-t)/10)
    s.append(u) 
    for d in s:
        sum = d**k + sum
    print(sum)
    '''
    if sum == n:
        return True
    else:
        return False 
    '''    
    return sum == n
print(armstrong(156,2))
print(armstrong(153,3))
