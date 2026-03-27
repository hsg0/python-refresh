class Main():
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        
    def user_info(self):
        return f"Name: {self.name}, Age: {self.age}, Location: {self.location}"
    
class UserScore(Main):
    def __init__(self, name, age, location, score):
        super().__init__(name, age, location)
        self.score = int(score)
    
    def average_score(self, list1):
        x = self.score/len(list1)*100
        print(f"Average Score: {x}%")
        
testList = [1, 2, 3, 4, 5]
user1 = UserScore("Alice", 30, "New York", 4)
user1.average_score(testList)

