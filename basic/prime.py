def prime(n):
    for a in range(2,n):
        if n % a == 0: 
            return False
    return True

for a in range(2,100):
    if prime(a):
        print(a)

'''print(prime(17))
print(prime(18))
print(prime(15))'''