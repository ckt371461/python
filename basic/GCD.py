def GCD1 (n1,n2):
    nn= max (n1,n2) 
    for n3 in range(nn,0,-1):
        if n1 % n3 == 0 and n2 % n3 == 0:
            return n3
print(GCD1(99,66))
