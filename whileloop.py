#while loops
#while loops are used to repeat a block of code as long as a condition is true
cost = int(input("Enter the cost of your meal: "))
total = 0
while cost != 0:
    total += cost
    cost = int(input("Enter the cost of your meal (enter 0 to finish): "))
print(f"The total cost of your meals is: ${total}")
total = total * 1.07
print(f"The total cost of your meals with tax is: ${total:.2f}")