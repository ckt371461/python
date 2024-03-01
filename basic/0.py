x = 23
y = 0 
print()
try:
    print(x/y)
except ZeroDivisionError as e:
    print('Not allowed to division by zero')
    print()
else:
    print('Something else went wrong')
finally:
    print('This is cleanup code')
print()