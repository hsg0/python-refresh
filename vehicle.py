
class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricCar():
    def __init__(self, battery_size):
        self.battery_size = battery_size
    
    def charge(self):
        print("Charging the electric car...")
        return "Electric car is now fully charged."
    
    def getRange(self):
        if self.battery_size == 75:
            return "The electric car can go approximately 260 miles on a full charge."
        elif self.battery_size == 100:
            return "The electric car can go approximately 315 miles on a full charge."
        else:
            return "Battery size not recognized. Range information unavailable."

class GasolineCar():
    def __init__(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity
    
    def refuel(self):
        print("Refueling the gasoline car...")
        return "Gasoline car is now fully refueled."
    
    def getRange(self):
        if self.fuel_capacity == 12:
            return "The gasoline car can go approximately 300 miles on a full tank."
        elif self.fuel_capacity == 15:
            return "The gasoline car can go approximately 375 miles on a full tank."
        else:
            return "Fuel capacity not recognized. Range information unavailable."
        
class HybridCar(Vehicle, ElectricCar, GasolineCar):
    def __init__(self, make, model, year, battery_size, fuel_capacity):
        Vehicle.__init__(self, make, model, year)
        ElectricCar.__init__(self, battery_size)
        GasolineCar.__init__(self, fuel_capacity)
        
car = HybridCar("Toyota", "Prius", 2020, 8.8, 11.3)
battery_range = car.getRange()
print(battery_range)