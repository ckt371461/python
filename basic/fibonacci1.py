def fibonacci(n):
    a = 1
    b = 1
    '''
    for i in range(0,n):
        c = a + b
        print(c)
        b = a
        a = c
    '''
    for s in range(0,int(n/2)):
        c = a + b
        a = c
        print(c)
        c = a + b
        b = c
        print(c)
fibonacci(10)
fibonacci(5)


