def map1(f, list):
    r = []
    for x in list:
        r.append(f(x))
    return r

def square(x):
    return x*x

sq = square
# print(map1(lambda x: x*x, [1,2,3]))
print(map1(square, [1,2,3]))
print(map1(sq, [1,2,3]))