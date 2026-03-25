# create a universal function 
# print("Welcome to the Travel Expense Calculator Bot!")
# print("Let's calculate your travel expenses.")
# name = input("What is your name? ").lower()
# age = int(input("What is your age? "))
# nationality = input("What is your nationality? ").lower()

# def personInfo(name, age, nationality):
#     print(f"Hello {name.title()}! You are {age} years old and your nationality is {nationality}.")
    
# personInfo(name, age, nationality)

# whereToTravel = input("Where are you traveling to? ").lower()
# costOfTrip = float(input("What is the estimated cost of your trip? "))
# for i in range(1, int(costOfTrip) + 1):
#     print(f"Processing cost step {i}...")

def totalPoints(gameScore):
    points = 0
    while gameScore != 0:
        if gameScore >= 1 and gameScore <= 10:
            points += 2
        elif gameScore >= 11 and gameScore <= 20:
            points += 5
        elif gameScore >= 21 and gameScore <= 30:
            points += 10
        else:
            print("Invalid score. Please enter a score between 1 and 30.")
        gameScore = int(input("Enter your next game score (or 0 to finish): "))
    return points
score = int(input("Enter your game score (or 0 to finish): "))
total_points = totalPoints(score)
print(f"Your total points are: {total_points}")