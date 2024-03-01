def sum(n):
    i = 1
    s = 0
    while i<=n:
        s = s + i
        i = i + 1
    return s  

# x = int(input("輸入一個整數 n，我會算 1+2+...+n, n="))
# print('sum(x)=', sum(x))

print('sum(10)=', sum(10))
