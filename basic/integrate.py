def integral(f, a, b, h = 0.0001):
    x = a
    area = 0
    while (x < b):
        area += f(x) * h
        x += h
    return area

print(integral(lambda x: x, 0, 1))
print(integral(lambda x: x*x, 0, 1))
