import sys

def bigest(d):
    k = -sys.maxsize-1
    for n in d:
        if n > k:
            k = n
    return k

print(bigest([0,8,3,9,50,8,3]))
print(bigest([-3, -1, -2]))