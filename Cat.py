class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def getLifeStage(self):
        if self.age <= 6:
            return "Kitten"
        elif self.age > 6 and self.age <= 24:
            return "Junior"
        elif self.age > 24 and self.age <= 72:
            return "Adult"
        elif self.age > 72 and self.age <= 120:
            return "Mature"
        elif self.age > 120 and self.age <= 168:
            return "Senior"
        else:
            return "Super-Senior"
    def answer(self):
        print(self.name + " is " + str(self.age/12) + "year(s) old, which means they're a " + self.getLifeStage())

Cats = int(input("How many cats do you have?: "))

allCats = []

for i in range(Cats):
    Age = int(input("How old is your cat? (in months): "))
    name = input("What is your cats name?: ")
    c1 = Cat(name, Age)
    allCats.append(c1)
  
for cat in allCats:
    cat.answer()


