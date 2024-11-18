# Task "Съедобное, несъедобное"


# Животные:
class Animal:
    alive = True
    fed = False

class Predator(Animal):
    def __init__(self, name):
        self.name = name
    def eat (self, food):
        if food.edible:
            self.fed = True
            print('16',self.fed)
        else:
            self.alive = False
            print('20', self.fed)

class Mammal(Animal):
    def __init__(self, name):
        self.name = name
    def eat (self, food):
        if food.edible:
            self.fed = True
        else:
            self.alive = False



# Растения:

class Plant:
    edible = False


class Flower(Plant):
    def __init__(self, name):
        self.name = name

class Fruit(Plant):
    edible = True
    def __init__(self, name):
        self.name = name

a1 = Predator('Тигра рогатая')
a2 = Mammal('Склиф')

p1 = Flower('Колючка')
p2 = Fruit('Дыня')

print(a1.name)
print(a2.name)
print(p1.name)
print(p2.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print('Сытость',a1.fed)
print('Жизнь', a1.alive)
print('Сытость',a2.fed)
print('Жизнь', a2.alive)
