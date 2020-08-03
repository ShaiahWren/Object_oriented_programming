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

# benji = Pet("Benji", 50, 20, 20, 1)
# lassie = Pet("Lassie", 50, 20, 20, 1)
# clifford = Pet("Old Yeller", 50, 20, 20, 1)


## Inheritance

class CuddlyPet(Pet):
    pass

benji = CuddlyPet("Benji", 50, 20)
print(benji.fullness, benji.happiness) ##50 20
# benji.be_alive()
print(benji.fullness, benji.happiness)

# from oop_16 import Pet  
# class CuddlyPet(Pet):
#     def cuddle(self, other_pet):
#         other_pet.get_love()


## Polymorphism

class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness

class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2

    def cuddle(self, other_pet):
        #super cuddle powers, activate!
        for i in range(self.cuddle_level):
            other_pet.get_love()
    