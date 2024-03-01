def factor(n):
    for a in range(1,n+1):
        if n % a == 0:
            print(a)
factor(10)
factor(80)
factor(3)