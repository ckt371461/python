class Element():
    def __init__(self,name,symbol,number):
        self.__name=name
        self.__symbol=symbol
        self.__number=number
#用__在前方來將name加密
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number
    def __str__(self):
        return f'name = {self.__name} , symbol = {self.__symbol} , number = {self.__number}'
Hydrogen1=Element('Hydrogen','H',1)
Hydrogen_dict={
    'name':'Hydrogen',
    'symbol':'H',
    'number':1}
Hydrogen2=Element(**Hydrogen_dict)
print(Hydrogen2)
print(Hydrogen2.name)