class Bear():
    def eat(self):
        return 'berries'
class Rabbit():
    def eat(self):
        return 'clover'
class Octotrope():
    def eat(self):
        return 'campers'
bear = Bear()
rabbit= Rabbit()
octotrope=Octotrope()
print(f'bear eat {bear.eat()} , rabbit eat {rabbit.eat()} , octotrope eat {octotrope.eat()}')