things=['mozzarella','cinderella','salmonella']
for i in range(len(things)):
    things[i] = things[i].capitalize()
things[0]=things[0].upper()
#沒有加上括號的話會變成物件 <built-in method upper of str object at 0x000002B1ACA60030>
things.remove('Salmonella')
#del things[-1] 這樣也可以
print(things)