import random

print("Welcome to the game, this is a number guessing game! \nYou got 5 attempts to guess the number between 50 and 100, let's start the game!!")

random_number = random.randrange(50, 100)

chances = 5

guess_counter = 0

while guess_counter < chances:

    try:
        my_guess = int(input("Please Enter Your Guess Number: "))
    except ValueError:
        print("\nInvalid Syntax. Please Enter Number!!\n")  
        continue

    guess_counter += 1

    
    if my_guess == random_number:
        print(f"The number is {random_number} and you found it right!! in the {guess_counter} attempts.")
        break

    elif guess_counter >= chances and my_guess != random_number:
        print(f"Ooops sorry, the number is {random_number}. Better luck next time")

    elif my_guess < random_number:
        print("Your guess number is very low , try again.")
    
    elif my_guess > random_number:
        print("Your guess number is very high , try again.")
    

      

