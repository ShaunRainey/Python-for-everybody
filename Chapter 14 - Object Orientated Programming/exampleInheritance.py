class PartyAnimal:
    def __init__(self,name):
        self.x = 0
        self.name = name
        print(f"{self.name} is constructed!")
    
    def party(self):
        self.x = self.x + 1
        print(f"{self.name} party count", self.x)

class FootballFan(PartyAnimal):
    def __init__(self, name):
        super().__init__(name)
        self.points = 0
    
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

j = FootballFan("Jim")
j.party()
j.touchdown()
