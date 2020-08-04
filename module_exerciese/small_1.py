class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys = []

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
        for toy in self.toys:
            self.happiness += toy.use()



class CuddlyPet(Pet):   
    def be_alive(self):
        super().be_alive()
        self.happiness -= self.mopiness/2
        

    def __str__(self):
        return "%s is extra cuddly" % self.name


print(CuddlyPet("Harriet"))