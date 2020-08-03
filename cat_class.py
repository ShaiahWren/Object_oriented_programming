class Cat:
    species = "mammal"
    legs = 4
    fur = "long-hair"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s is %d years old" % (self.name, self.age)

    # Instance method

    def eat(self, cans_of_food):
        self.cans_of_food = cans_of_food
        return "%s ate %d cans of food" % (self.name, self.cans_of_food)

guster = Cat("Guster", 10)
beans = Cat("Beans", 11)
        
print(guster.eat(1))
print(beans.eat(2))