from Animal import Animal
from AnimalShelter import AnimalShelter

def test_set_attributes():
    a = Animal()

    assert a.species == None
    a.setSpecies("lizard")
    assert a.species == "LIZARD"
    a.setSpecies("penguin")
    assert a.species == "PENGUIN"

    assert a.weight == None
    a.setWeight(5)
    assert a.weight == 5
    a.setWeight(8)
    assert a.weight == 8

    assert a.age == None
    a.setAge(3)
    assert a.age == 3
    a.setAge(2)
    assert a.age == 2

    assert a.name == None
    a.setName("scales")
    assert a.name == "SCALES"
    a.setName("flipper")
    assert a.name == "FLIPPER"

def test_toString():
    r = Animal("dog", 12.2, 2, "Ruffles")
    t = Animal("whale", 8000, 15, "Big Blue")
    y = Animal("LIZarD", 5, 4, "scalEs")
    
    assert r.toString() == "Species: DOG, Name: RUFFLES, Age: 2, Weight: 12.2"
    assert t.toString() == "Species: WHALE, Name: BIG BLUE, Age: 15, Weight: 8000"
    assert y.toString() == "Species: LIZARD, Name: SCALES, Age: 4, Weight: 5"

def test_Add_Exist():
    v = AnimalShelter()
    v.addAnimal(Animal("Koala", 45, 24, "Jingo"))
    assert v.doesAnimalExist(Animal("Koala", 45, 24, "Jingo")) == True
    v.addAnimal(Animal("BIRD", 5, 6, "KIWI"))
    assert v.doesAnimalExist(Animal("BIRD", 5, 6, "KIWI")) == True
    v.addAnimal(Animal("ZEBRA", 200, 6, "MARTY"))
    assert v.doesAnimalExist(Animal("ZEBRA", 200, 6, "MARTY")) == True

def test_getAnimalsBySpecies():  
    v = AnimalShelter()
    v.addAnimal(Animal("Koala", 45, 24, "Jingo"))
    v.addAnimal(Animal("BIRD", 5, 6, "KIWI"))
    v.addAnimal(Animal("ZEBRA", 200, 6, "MARTY"))

    assert v.getAnimalsBySpecies("Koala") == "Species: KOALA, Name: JINGO, Age: 24, Weight: 45"
    assert v.getAnimalsBySpecies("BirD") == 'Species: BIRD, Name: KIWI, Age: 6, Weight: 5'
    assert v.getAnimalsBySpecies("zeBra") == 'Species: ZEBRA, Name: MARTY, Age: 6, Weight: 200'
    
def test_Remove_Exist():
    v = AnimalShelter()
    v.addAnimal(Animal("Koala", 45, 24, "Jingo"))
    v.addAnimal(Animal("BIRD", 5, 6, "KIWI"))
    v.addAnimal(Animal("ZEBRA", 200, 6, "MARTY"))

    assert v.removeAnimal(Animal("Koala", 45, 24, "Jingo")) == None
    assert v.doesAnimalExist("Koala") == False
    assert v.removeAnimal(Animal("BIRD", 5, 6, "KIWI")) == None
    assert v.doesAnimalExist("Bird") == False
    assert v.removeAnimal(Animal("ZEBRA", 200, 6, "MARTY")) == None
    assert v.doesAnimalExist("zebra") == False
