from Animal import Animal

class AnimalShelter:
    def __init__(self):
        self.AnimalShelter = {}
    
    def addAnimal(self, animal):
        if animal.species not in self.AnimalShelter:
            self.AnimalShelter[animal.species] = [animal]
        else:
            self.AnimalShelter[animal.species].append(animal)

    def removeAnimal(self, animal):
        if animal.species in self.AnimalShelter:
            for animals in self.AnimalShelter[animal.species]:
                if animals.toString() == animal.toString():
                    self.AnimalShelter[animal.species].remove(animal)

    def getAnimalsBySpecies(self, species):
        x = ""
        species = species.upper()
        if species not in self.AnimalShelter:
            return x
        else:
            length = len(self.AnimalShelter[species])
            for i in range(0, length):
                animal = self.AnimalShelter[species]
                if i == length-1:
                    x += animal[i].toString()
                else:
                    x += animal[i].toString() + "\n"
            return x
    
    def doesAnimalExist(self, animal):
        if animal.species in self.AnimalShelter:
            for animals in self.AnimalShelter[animal.species]:
                if animals.toString() == animal.toString():
                    return True
        return False