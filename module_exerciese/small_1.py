class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys = []

    def __str__(self):
        return """
            %s:
            Fullness: %d
            Happiness: %d
            Hunger: %d
            Mopiness: %d
        """ % (self.name, self.fullness, self.happiness, self.hunger, self.mopiness)

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
        print("Be alive in Pet class for %s" % self.name)
 


class CuddlyPet(Pet):   
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5, cuddle_level=1):
        super().__init__(name, fullness=fullness, happiness=happiness, hunger=hunger, mopiness=mopiness)
        self.cuddle_level = cuddle_level  

    def __str__(self):
        return """
        %s: 
        Fullness: %d
        Happiness: %d
        Hunger: %d
        Mopiness: %d
        Cuddle level: %s
        """ % (self.name, self.fullness, self.happiness, self.hunger, self.mopiness, self.cuddle_level)

    def be_alive(self):
        super().be_alive()
        self.happiness -= self.mopiness/2
        print("Be alive in CuddlyPet class for %s" % self.name)

# print(CuddlyPet("Harriet", 50, 100, 30, 0, "Extra cuddly"))

guster= Pet("Guster", 10, 100, 200, 0)
beans = CuddlyPet("Beans", 20, 100, 200, 0, "Extra Cuddly")

guster.be_alive()
beans.be_alive()