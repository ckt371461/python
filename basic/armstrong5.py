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
    return sum == n

def armstrong_range(lo, hi):
    lo, hi = min(lo,hi), max(lo,hi)
    for i in range(lo, hi+1):
        if (armstrong(i)):
            print(i)


armstrong_range(50, 200)
armstrong_range(1000, 2000)
# print(armstrong(156))
# print(armstrong(153))
