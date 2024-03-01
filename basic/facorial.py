# f(1) = 1
# f(n) = f(n-1)*n
def facorial1(n):
    if n == 1:
        return 1
    return facorial1(n-1)*n
print(facorial1(5))
    