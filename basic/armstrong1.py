def armstrong(n,k): # 檢查 n 是否為 k 階的阿姆斯壯數
    s = []
    sum =0
    u = n
    while n >= 10:
        t = n % 10 
        s.append(t)
        n = int((n-t)/10)
    s.append(n) 
    for d in s:
        sum = d**k + sum
    print(sum)
    if sum == u:
        return True
    else:
        return False 

print(armstrong(156,2))
print(armstrong(153,3))
