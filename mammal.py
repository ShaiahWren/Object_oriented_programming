class Mammal:
    def __init__(self, type_of_mammal, breed, legs):
        self.type_of_mammal = type_of_mammal
        self.breed = breed
        self.legs = legs

gus = Mammal("cat", "mixed", 4)

class Cat(Mammal):
    def __init__(self, type_of_mammal, breed, legs, fur):
        super().__init__(type_of_mammal, breed, legs)
        self.fur = fur
        