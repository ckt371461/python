def power2(n):
    return 2**n

result = list(map(lambda n: 2 ** n, range(10)))
print(result)

result = list(map(power2, range(10)))
print(result)

