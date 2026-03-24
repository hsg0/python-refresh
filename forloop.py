# simple passcode checker using for loop

# passcode = input("Enter the passcode: ")
# invalid = "!@#$%^&*()_+"
# for letter in passcode:
#     if letter in invalid:
#         print("Invalid passcode")
#         break
#     elif letter.lower() in passcode:
#         print("Passcode accepted")
#         break
#     else:
#         print("Passcode rejected")
#         break

# program that counts vowels and prints the number of vowels

# vowels = "aeiouAEIOU"
# const = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
# word = input("Enter a word: ")
# vowel_count = 0
# const_count = 0
# for letter in word:
#     if letter in vowels:
#         vowel_count += 1
#     elif letter in const:
#         const_count += 1
# print(f"The number of vowels in the word is: {vowel_count}")
# print(f"The number of consonants in the word is: {const_count}")

#  create a program that checks for a valid phone number

# phone_number = input("Enter a phone number: ")
# valid = "0123456789+"

# for i in phone_number:
#     if i not in valid:
#         print("Invalid phone number")
#         break


#  program that takes a number of gas for each guest ask their age and name if the guest is over 21 welcome to user and allow them to drink if the user is below 21 drinking is not allowed

# guests = int(input("Enter the number of guests: "))
# for i in range(guests):
#     name = input("Enter the name of the guest: ")
#     age = int(input("Enter the age of the guest: "))
#     if age >= 21:
#         print(f"Welcome {name}, you are allowed to drink.")
#     else:
#         print(f"Sorry {name}, you are not allowed to drink.")


# user has 5 chances to guess a number to login to a system. 
import random

numberToGuess = random.randint(1, 10)
chances = 5

for i in range(chances):
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == numberToGuess:
        print("Congratulations! You guessed the number.")
        break
    elif guess < numberToGuess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print(f"Sorry, you've used all your chances. The number was {numberToGuess}.")
