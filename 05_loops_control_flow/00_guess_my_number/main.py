import random

print("Welcome to the game, this is a number guessing game! \nYou got 5 attempts to guess the number between 50 and 100, let's start the game!!")

random_number = random.randint(50, 100)
chances = 5
guess_counter = 0

def main():

    while guess_counter <= chances:

        try:
            number = int(input("Guess my number..."))

        except ValueError:
            print("invalid Syntax. Please enter number")

        if number > random_number:
            print("Your guess is too high.")

        elif number < random_number:
            print("Your guess is too low.")

        elif number == random_number:
            print(f"Congrats! The number was: {random_number}.")
            break

        elif guess_counter >= chances and number != random_number:
            print(f"Ooops sorry, the number is {random_number}. Better luck next time")

if __name__ == "__main__":
    main()    