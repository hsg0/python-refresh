# class animal:
#     def __init__(self, creatureType):
#         self.creatureType = creatureType
        
#     def numberOfLegs(self):
#         legs = int(input("Enter the number of legs: "))
#         return legs
    
#     def numberOfArms(self):
#         arms = int(input("Enter the number of arms: "))
#         return arms
    
#     def determineAnimal(self):
#         legs = self.numberOfLegs()
#         arms = self.numberOfArms()
        
#         if arms == 0 and legs == 0:
#             print("No arms or legs - it must be a fish or a snake")
#         elif arms == 2 and legs == 2:
#             print("It might be a human or a bird")
#         elif arms == 0 and legs == 4:
#             print("It might be a dog, cat, or other quadruped")
#         elif arms == 0 and legs == 2:
#             print("It might be a bird")
#         else:
#             print(f"Animal with {arms} arms and {legs} legs")
    
# class dog(animal):
#     pass
# class Vehicle():
#     def __init__(self, make, model, year, price):
#         self.make = make
#         self.model = model
        
#     def getMake(self):
#         if self.make == "Chevy" or self.make == "Ford" or self.make == "Dodge" or self.make == "Tesla":
#             return "American Brand"
#         if self.make == "Toyota" or self.make == "Honda" or self.make == "Nissan":
#             return "Japanese Brand"
#         if self.make == "BMW" or self.make == "Mercedes" or self.make == "Audi":
#             return "German Brand"
#         else:
#             return "Unknown Brand"
        
#     def getModel(self):
#         return self.model
    
#     def getVehicleYear(self):
#         self.year = int(input("Enter the vehicle's year: "))
#         return self.year
    
#     def getVehiclePrice(self):
#         self.price = float(input("Enter the vehicle's price: "))
#         return self.price

# class Car(Vehicle):
#     def __init__(self, make, model, year, price, numDoors):
#         super().__init__(make, model, year, price)
#         self.numDoors = numDoors
    
#     def getNumDoors(self):
#         return self.numDoors
    
class Agent():
    def __init__(self, name, age, agency):
        self.name = name
        self.age = age
        self.agency = agency
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getAgency(self):
        return self.agency
    
class Spy(Agent):
    def __init__(self, name, age, agency, codeName):
        super().__init__(name, age, agency)
        self.codeName = codeName
    
    def getCodeName(self):
        return self.codeName
    
agent1 = Agent("John Doe", 35, "CIA")
spy1 = Spy("Jane Smith", 30, "MI6", "Shadow")
print(f"Agent Name: {agent1.getName()}, Age: {agent1.getAge()}, Agency: {agent1.getAgency()}")
print(f"Spy Name: {spy1.getName()}, Age: {spy1.getAge()}, Agency: {spy1.getAgency()}, Code Name: {spy1.getCodeName()}")
