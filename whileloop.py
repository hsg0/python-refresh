#while loops
#while loops are used to repeat a block of code as long as a condition is true
# cost = int(input("Enter the cost of your meal: "))
# total = 0
# while cost != 0:
#     total += cost
#     cost = int(input("Enter the cost of your meal (enter 0 to finish): "))
# print(f"The total cost of your meals is: ${total}")
# total = total * 1.07
# print(f"The total cost of your meals with tax is: ${total:.2f}")


# counter = 0
# while counter < 5:
#     print(f"Counter is at: {counter}")
#     counter += 1
#     print("This will print until the counter reaches 5.")
# print("Counter has reached 5, exiting the loop.")

# tries = 0
# code = ""

# while tries < 5 and code != 'python':
#     code = int(input("Enter the secret code: "))
#     tries += 1
    
# if code == 'python':
#     print("Congratulations! You've entered the correct code.")
# else:
#     print("Sorry, you've used all your tries. Better luck next time!")

trainTicket = input("Enter 1 - Book a train ticket, 2 - Cancel a train ticket, 3 - Check train schedule: ") 
i = 1

while trainTicket != '1':
    if trainTicket == '2':
        print("You have chosen to cancel a train ticket.")
    elif trainTicket == '3':
        print("You have chosen to check the train schedule.")
    else:
        print("Invalid option. Please enter 1, 2, or 3.")
    
    if i >= 5:
        print("Too many invalid attempts. Exiting the program.")
        break
    
    trainTicket = input("Enter 1 - Book a train ticket, 2 - Cancel a train ticket, 3 - Check train schedule: ")
    i += 1