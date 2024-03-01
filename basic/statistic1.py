import random
b = []
for a in range(100):
    b.append(random.randint(0,9))   
print(b)

s = [0]*10
for c in b:
    s[c] = s[c] + 1 

print(s)