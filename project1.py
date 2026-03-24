cities_to_travel = [
    "Jericho",  # One of the oldest cities in the world
    "Athens",
    "Rome",
    "Istanbul",
    "Beijing",
    "Kyoto",
    "Paris",
    "London",
    "New York",
    "Tokyo",
    "Dubai",
    "Cairo",
    "Baghdad",
    "Damascus",
    "Jerusalem",
    "Alexandria",
    "Varanasi",
    "Lisbon",
    "Venice",
    "Florence",
    "Prague",
    "Vienna",
    "Budapest",
    "Berlin",
    "Madrid",
    "Barcelona",
    "Moscow",
    "St. Petersburg",
    "Hanoi",
    "Bangkok",
    "Singapore",
    "Seoul",
    "Mumbai",
    "Cape Town",
    "Buenos Aires",
    "Rio de Janeiro",
    "Mexico City",
    "Lima",
    "Santiago",
    "Toronto",
    "San Francisco",
    "Los Angeles",
    "Chicago",
    "Sydney",
    "Melbourne",
    "Auckland",
    "Kuala Lumpur",
    "Jakarta",
    "Manila",
    "Taipei"
]

# create a bot traveling to different cities and calculating expenses based on user input. The bot should ask the user for the city they are traveling to, the number of days they will stay, and their daily expenses. The bot should then calculate the total expenses for the trip and provide a summary to the user.
print("Welcome to the Travel Expense Calculator Bot!")
print("Let's calculate your travel expenses.")

# lets plan your trip! Here are some cities you can choose from:
enter = input("Press any key to start or 0 to exit: ").strip()
while enter != "0":
    print("Here is a list of cities you can travel to:")
    for city in cities_to_travel:
        print(city)
    city = input("Enter the city you are traveling to: ").title()
    if city not in cities_to_travel:
        print("Sorry, we don't have information for that city. Please choose from the list.")
        continue
    try:
        days = int(input("Enter the number of days you will stay: "))
        
        transport = input("Transport: Plane/Train or Car: ").lower()
        if transport == 'plane':
            class_type = input("Which fare would you like? (First/Business/Economy): ").lower()
            luggage = int(input("Enter baggage weight in KG: "))
            if luggage >= 21 and class_type == "business" or class_type == "first":
                print("Great, you can have more baggage with these classes")
            elif luggage < 21 and class_type == "business" or class_type == "first":
                print("You can bring more if you want!")
            else:
                print("Warning, you may have too much!")
        elif transport == 'train':
            seat_class = input("Economy or business: ").lower()
            if seat_class == 'business':
                print("Great! More comfort your way.")
            elif seat_class == 'economy':
                print("You save more this way!")
            else:
                print("We don't have that class.")
        elif transport == 'car':
            print("Road trips are fun!")
            num_people = int(input("Enter the number of people traveling: "))
        
        flight_expense = float(input("Enter your flight expenses: "))
        luggage_expense = float(input("Enter your luggage expenses: "))
        hotel_expense = float(input("Enter your daily hotel expenses: "))
        extra_expense = float(input("Enter your daily extra expenses (food, entertainment, etc.): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue
    nextCityToTravel = input("Do you want to plan another trip? (yes/no): ").lower()
    totalExpenses = flight_expense + luggage_expense + (extra_expense * days) + (hotel_expense * days)
    print(f"Your total expenses for your trip to {city} will be: ${totalExpenses:.2f}")
    if nextCityToTravel == "yes":
        continue
    else:
        break
print("Thank you for using the Travel Expense Calculator Bot! Safe travels!")


