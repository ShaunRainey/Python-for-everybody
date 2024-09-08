class PartyAnimal:
    def __init__(self,name):
        self.x = 0
        self.name = name
        print(f"{self.name} is constructed!")
    
    def party(self):
        self.x = self.x + 1
        print(f"{self.name} party count", self.x)

s = PartyAnimal("Sally")
j = PartyAnimal("Jim")
s.party()
j.party()
s.party()
print(s.name)