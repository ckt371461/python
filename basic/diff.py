def diff(f, x, h=0.00001):
    return (f(x+h)-f(x)) / h

# square = lambda x: x*x
def square(x):
    return x*x

print(diff(square, 1.0))
