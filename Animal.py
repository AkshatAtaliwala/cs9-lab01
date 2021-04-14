class Animal: 
    def __init__(self, species = None, weight = None, age = None, name = None):
            if species != None:
                self.species = str(species).upper()
            else:
                self.species = None
            self.weight = weight
            self.age = age
            if name != None:
                self.name = str(name).upper()
            else:
                self.name = None

    def setSpecies(self, species):
        self.species = str(species).upper()

    def setWeight(self, weight):
        self.weight = weight

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name = str(name).upper()
    
    def toString(self):
        return ("Species: {}, Name: {}, Age: {}, Weight: {}"
        .format(self.species, self.name, self.age, self.weight))
