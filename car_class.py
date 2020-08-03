class Car:
    wheels = 4
    axles = 2

    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def __str__(self):
        return "%s is a %s and she is a model %d" % (self.name, self.model, self.year)

    def burn_fuel(self, fuel):
        self.fuel = fuel
        return "%s burned %d gallons of fuel on our last trip." % (self.name, self.fuel)

    def flip(self, flips):
        self.flips = flips
        return "%s did %d flips when she fell off the bridge." % (self.name, self.flips)



henrietta = Car("Henrietta", "Volvo", 2000)
acadia = Car("Acadia", "Volkswagon", 2019)

print(henrietta)
print(acadia)

print(henrietta.burn_fuel(30))
print(acadia.burn_fuel(20))

print(henrietta.flip(5))
print(acadia.flip(7))