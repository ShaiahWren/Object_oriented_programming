class Pet:
    def __init__(self, name, fullness, happiness):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness



cujo = Pet("Cujo", 50, 20)
print(cujo.name)

benji = Pet("Benji", 50, 100)
print(benji.name)

## default argument values

class Pet():
    def __init__(self, name, fullness = 50, happiness = 50):
        self.name = name  
        self.fullness = fullness
        self.happiness = happiness

cujo = Pet("Cujo")
print(cujo.name)

benji = Pet("Benji")
print(benji.name)

## Methods

class Pet:
    def __init__(self, name, fullness=50, happiness=50):
        self.name = name  
        self.fullness = fullness
        self.happiness = happiness

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

cujo = Pet("Cujo")
cujo.eat_food()
print(cujo.fullness)  ## 80
print(cujo.happiness) ## 50

benji = Pet("Benji")
benji.get_love()
print(cujo.fullness)  ## 50
print(benji.happiness) ## 80



## Encapsulation

class Pet:
    def __init__(self, name, fullness=50, happiness=50):
        self.name = name  
        self.fullness = fullness
        self.happiness = happiness

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def be_alive(self, hunger, mopiness):
        self.fullness -= 5
        self.happiness -+ 5


