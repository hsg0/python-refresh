# class animal():
#     def __init__(self, name, pet, sound):
#         self.name = name
#         self.pet = pet
#         self.sound = sound
        
#     def speak(self):
#         print(self.sound)
        
#     def pet_info(self):
#         print(f"{self.name} has a {self.pet} that says {self.sound}.")
        
# dog = animal("Alice", "dog", "Woof")
# cat = animal("Bob", "cat", "Meow")

# dog.speak()  # Output: Woof
# cat.speak()  # Output: Meow

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def printInfo(self):
        print(f"Length: {self.length}, Width: {self.width}")
        
    def calPreimeter(self):
        self.perimeter = 2 * (self.length + self.width)
        return self.perimeter
    
    def calArea(self):
        self.area = self.length * self.width
        return self.area
    
    def update(self, length):
        self.length = length
        print(f"Updated Length: {self.length}")
        
a = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the width of the rectangle: "))

rect1 = Rectangle(a, b)
rect1.printInfo()
print(f"Perimeter: {rect1.calPreimeter()}")
print(f"Area: {rect1.calArea()}")