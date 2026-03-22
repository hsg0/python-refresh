# practice with nested conditions
# nested conditions are conditions within conditions
# example 1
import random
import time 
# want = input("Do you want to watch a movie? (yes/no) ").strip().lower() == "yes"
# genre = input("What genre do you want to watch? (comedy, sci-fi, documentary, drama, action, horror) ").strip().lower()

# recommendations = {
#     'comedy': ['superbad', 'the hangover', 'bridesmaids', 'step brothers', 'anchorman', 'mean girls'],
#     'sci-fi': ['the martian', 'interstellar', 'inception', 'blade runner 2049', 'arrival', 'the matrix'],
#     'documentary': ['blackfish', 'the social dilemma', 'free solo', 'making a murderer', 'planet earth', 'won\'t you be my neighbor'],
#     'drama': ['the big short', 'the wolf of wall street', 'the shawshank redemption', 'forrest gump', 'the godfather', 'fight club'],
#     'action': ['mad max fury road', 'john wick', 'die hard', 'the dark knight', 'gladiator', 'mission impossible'],
#     'horror': ['get out', 'a quiet place', 'hereditary', 'the conjuring', 'it', 'midsommar']
# }

# if want:
#     if genre in recommendations:
#         movie = random.choice(recommendations[genre])
#         print(f"You should watch: {movie}")
#     else:
#         print("Sorry, we don't have recommendations for that genre.")
# else:
#     print("Maybe next time!")

# accomodation = str(input("Enter resort or hotel")).strip().lower()
# if accomodation == 'resort':
#     maxPrice = int(input("enter max price:"))
#     if maxPrice >= 5000:
#         print("resorts selected over $5000")
#     else:
#         print('resorts selected under $5000')
# elif accomodation == 'hotel':
#     maxPrice = int(input("enter max price:"))
#     if maxPrice >= 2000:
#         print("hotels selected over $2000")
#     else:
#         print('hotels selected under $2000')
# else:
#     print("invalid accomodation type")
        
        
whatTime = random.randint(0, 23)
cost = random.randint(1, 10000)

if whatTime >= 7 and whatTime <= 10:
    print("Good morning! We have some great breakfast options for you.")
    if cost >= 20:
        print("You can enjoy our full breakfast buffet for $20 or more.")
    else:
        print("We have a light breakfast menu available for under $20.")
elif whatTime > 10 and whatTime <= 14:
    print("Good afternoon! We have some delicious lunch options for you.")
    if cost >= 30:
        print("You can enjoy our gourmet lunch menu for $30 or more.")
    else:
        print("We have a quick and tasty lunch menu available for under $30.")
elif whatTime > 14 and whatTime <= 18:
    print("Good evening! We have some fantastic dinner options for you.")
    if cost >= 50:
        print("You can indulge in our fine dining experience for $50 or more.")
    else:
        print("We have a great selection of dinner options available for under $50.")
else:
    print("Sorry, we are closed. Our operating hours are from 7 AM to 6 PM.")