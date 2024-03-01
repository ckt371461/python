# for x in range(-10000.0,10000.0,0.01):
x = -1000.0
while x < 1000.0:
    a = 3*(x**2) - 6*x -30
    if abs(a) <= 0.01:
        print('x=', x)
    x += 0.001


