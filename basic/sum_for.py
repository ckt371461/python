def sum(n):
    s = 0
    for x in range(1,n+1): 
        s = s + x
    return s
# x = int(input("輸入一個整數 n，我會算 1+2+...+n, n="))
# print('sum(x)=', sum(x))

print('sum(10)=', sum(10))
