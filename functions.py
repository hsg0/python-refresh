# def grade(score):
#     print("Your score is:", score)
#     if score >= 90:
#         print("Grade: A")
#     elif score >= 80:
#         print("Grade: B")
#     elif score >= 70:           
#         print("Grade: C")
#     elif score >= 60:
#         print("Grade: D")
#     else:
#         print("Grade: F")
# score = float(input("Enter your score: "))
# grade(score)


# def calculate_total_expenses(flight_expense, luggage_expense, extra_expense, hotel_expense, days):
#     total_expenses = flight_expense + luggage_expense + (extra_expense * days) + (hotel_expense * days)
#     return total_expenses
# flight_expense = float(input("Enter your flight expenses: "))
# luggage_expense = float(input("Enter your luggage expenses: "))
# hotel_expense = float(input("Enter your daily hotel expenses: "))
# extra_expense = float(input("Enter your daily extra expenses (food, entertainment, etc.): "))
# days = int(input("Enter the number of days you will stay: "))
# totalExpenses = calculate_total_expenses(flight_expense, luggage_expense, extra_expense, hotel_expense, days)
# print(f"Your total expenses for your trip will be: ${totalExpenses:.2f}")

# def flightExpense(price, tax_rate):
#     upgrade = input("Do you want to upgrade your flight? (yes/no): ").lower()
#     class_type = "economy"  # Default class type
#     if upgrade == "yes":
#         class_type = input("Which fare would you like? (First/Business/Economy): ").lower()
#         if class_type == "first":
#             price *= 1.5
#         elif class_type == "business":
#             price *= 1.2
#         else:
#             class_type = "economy"
#             price *= 1.1
#     baggage = int(input("Enter baggage weight in KG: "))
#     if baggage >= 21 and (class_type == "business" or class_type == "first"):
#         print("Great, you can have more baggage with these classes")
#     elif baggage < 21 and (class_type == "business" or class_type == "first"):
#         print("You can bring more if you want!")
#     else:
#         print("Warning, you may have too much!")
    
#     if upgrade == "yes" and baggage >= 21:
#         tax_rate *= 1.5
#     elif upgrade == "yes" and baggage < 21:
#         tax_rate *= 1.2
#     elif upgrade == "no" and baggage >= 21:
#         tax_rate *= 1.1
    
#     total_price = price + (price * tax_rate)
#     return total_price

# def mortgage_calculator(homeValue, downPayment, interestRate, loanTerm):
#     loanAmount = homeValue - downPayment
#     monthlyInterestRate = interestRate / 100 / 12
#     numberOfPayments = loanTerm * 12
#     monthlyPayment = (loanAmount * monthlyInterestRate) / (1 - (1 + monthlyInterestRate) ** -numberOfPayments)
#     return monthlyPayment
# homeValue = float(input("Enter the home value: "))
# downPayment = float(input("Enter the down payment: "))
# interestRate = float(input("Enter the annual interest rate (in %): "))
# loanTerm = int(input("Enter the loan term (in years): "))
# monthlyPayment = mortgage_calculator(homeValue, downPayment, interestRate, loanTerm)
# print(f"Your monthly mortgage payment will be: ${monthlyPayment:.2f}")  

# def terminal1():
#     print("Departing from Terminal 1. Please proceed to check-in.")
#     flightCheck()
    
# def terminal2():
#     print("Departing from Terminal 2. Please proceed to check-in.")
#     flightCheck()
    
# def terminal3():
#     print("Departing from Terminal 3. Please proceed to check-in.")
#     flightCheck()
    
# def flightCheck():
#     answer = input("Do you have your flight ticket and ID ready? (yes/no): ").lower()
#     if answer == "yes":
#         print("Great! You are ready to check in.")
#     else:
#         print("Please make sure to have your flight ticket and ID ready before checking in.")
#     if answer == "yes":
#         print("Proceeding to security check.")
#         flightType = input("Is your flight domestic or international? (domestic/international): ").lower()
#         flightcost = float(input("Enter your flight cost: "))
#         if flightType == "domestic" and flightcost < 200:
#             print("You are eligible for a discount on your flight.")
#         elif flightType == "international" and flightcost >= 500:
#             print("You are eligible for a discount on your flight.")
#         else:
#             print("You are not eligible for a discount on your flight.")
            
# def flightSelection():
#     print("Please choose from the following domestic flight options in Canada:")
#     print("1. Victoria")
#     print("2. Vancouver")
#     print("3. Calgary")
#     print("4. Edmonton")
#     print("5. Regina")
#     print("6. Saskatoon")
#     print("7. Winnipeg")
#     print("8. Toronto")
#     print("9. Ottawa")
#     print("10. Montreal")
#     print("11. Quebec City")
#     print("12. Halifax")
#     print("13. St. John's")
#     print("14. Charlottetown")
#     print("15. Yellowknife")
#     print("16. Whitehorse")
#     print("17. Iqaluit")
    
#     choice = input("Enter the number corresponding to your destination: ")
    
#     cities = {
#         "1": "Victoria",
#         "2": "Vancouver",
#         "3": "Calgary",
#         "4": "Edmonton",
#         "5": "Regina",
#         "6": "Saskatoon",
#         "7": "Winnipeg",
#         "8": "Toronto",
#         "9": "Ottawa",
#         "10": "Montreal",
#         "11": "Quebec City",
#         "12": "Halifax",
#         "13": "St. John's",
#         "14": "Charlottetown",
#         "15": "Yellowknife",
#         "16": "Whitehorse",
#         "17": "Iqaluit"
#     }
    
#     if choice in cities:
#         print(f"You have selected a flight to {cities[choice]}.")
#         return choice
#     else:
#         print("Invalid selection. Please try again.")
#         return None
    

# # lets check for flights
# def check_flight():
#     flight_type = input("Is your flight domestic or international? (domestic/international): ").lower()
#     #flight_cost = float(input("Enter your flight cost: "))
#     if flight_type == "domestic":
#         print("You have a domestic flight.")
#         selectFlight = input("Do you want to select a flight? (yes/no): ").lower()
#         if selectFlight == "yes":
#             print("You have selected to select a flight.")
#             selected = flightSelection()
#             if selected == "1":
#                 print("You have selected a flight to Victoria.")
#             elif selected == "2":
#                 print("You have selected a flight to Vancouver.")
#             elif selected == "3":
#                 print("You have selected a flight to Calgary.")
#             elif selected == "4":                
#                 print("You have selected a flight to Edmonton.")
#             elif selected == "5":
#                 print("You have selected a flight to Regina.")
#             elif selected == "6":
#                 print("You have selected a flight to Saskatoon.")
#             elif selected == "7":
#                 print("You have selected a flight to Winnipeg.")
#             elif selected == "8":
#                 print("You have selected a flight to Toronto.")
#             elif selected == "9":
#                 print("You have selected a flight to Ottawa.")
#             elif selected == "10":
#                 print("You have selected a flight to Montreal.")
#             elif selected == "11":
#                 print("You have selected a flight to Quebec City.")
#             elif selected == "12":
#                 print("You have selected a flight to Halifax.")
#             elif selected == "13":
#                 print("You have selected a flight to St. John's.")
#             elif selected == "14":   
#                 print("You have selected a flight to Charlottetown.")
#             elif selected == "15":
#                 print("You have selected a flight to Yellowknife.")
#             elif selected == "16":
#                 print("You have selected a flight to Whitehorse.")
#             elif selected == "17":
#                 print("You have selected a flight to Iqaluit.")
#             else:
#                 print("Invalid selection. Please try again.")
#         else:
#             print("You have selected not to select a flight.")
#     elif flight_type == "international":
#         print("You have an international flight.")
#     else:
#         print("Invalid flight type. Please enter 'domestic' or 'international'.")


# # get weight in kg
# def get_weight_kg():
#     weight_kg = float(input("Enter your weight in kilograms: "))
#     return weight_kg

# # get weight in pounds
# def get_weight_pounds():
#     weight_pounds = float(input("Enter your weight in pounds: "))
#     return weight_pounds

# # create a function to convert kg to pounds and vice versa
# def convert_weight(weight, from_unit, to_unit):
#     if from_unit == "kg" and to_unit == "pounds":
#         return weight * 2.20462
#     elif from_unit == "pounds" and to_unit == "kg":
#         return weight / 2.20462
#     else:
#         print("Invalid units. Please use 'kg' or 'pounds'.")
#         return None

# # calculate bmi using the formula: BMI = weight (kg) / (height (m))^2
# def calculate_bmi(weight_kg, height_m):
#     bmi = weight_kg / (height_m ** 2)
#     return bmi

# # display the calculated BMI and provide feedback on the weight category (underweight, normal weight, overweight, obese) based on standard BMI ranges.
# def display_bmi_category(bmi):
#     print(f"Your BMI is: {bmi:.2f}")
#     if bmi < 18.5:
#         print("You are underweight.")
#     elif 18.5 <= bmi < 24.9:
#         print("You have a normal weight.")
#     elif 25 <= bmi < 29.9:
#         print("You are overweight.")
#     else:
#         print("You are obese.")