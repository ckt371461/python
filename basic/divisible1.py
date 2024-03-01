list = [1,3,8,99,564,77,20,400]
def divisible(n):
    kk = []
    for num in list:
        if num % n == 0:
            kk.append(num)
    return kk

kk=divisible(3)
print(kk)