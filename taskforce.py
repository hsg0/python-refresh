class Animal():
    def __init__(self, region, animal_type, color, lethal):
        self.region = region
        self.animal_type = animal_type
        self.color = color
        self.lethal = lethal
        
    def animal_bio(self):
        return f"{self.animal_type} is a {self.color} animal that is found in {self.region}. It is {'lethal' if self.lethal else 'not lethal'}."
    
class clinic(Animal):
    def animal_info(self):
        print(f"Animal Type: {self.animal_type}")
        print(f"Region: {self.region}")
        
    def search(self, animals):
        region = input("Enter the region to search for animals: ")
        for animal in animals:
            if animal.region == region:
                print(f'{animal.animal_type} found in {region}.')