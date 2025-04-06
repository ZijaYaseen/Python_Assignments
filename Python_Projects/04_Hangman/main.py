import random
from words import words
import string

def valid_words(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    print("Welcome to Hangman!")

    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left and you have used these letters: {' '.join(used_letters)}")

        # Show current word progress
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        # Get user input
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Good job! '{user_letter}' is in the word.")
            else:
                lives -= 1
                print(f"Sorry! '{user_letter}' is not in the word.")
        elif user_letter in used_letters:
            print("You have already used that letter. Try a different one.")
        else:
            print("Invalid input. Please enter a valid letter.")

    # Game result
    if lives == 0:
        print(f"\nYou lost! The word was: {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word}")

hangman()
