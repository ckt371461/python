price = input('How much did you pay? ')
price = float(price)
if price >= 1.00:
    tax = .7
else:
    tax=0
print('Tax rate is : ' + str(tax))
    