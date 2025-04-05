AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    
    while True:
        print(f"Please type the following affirmation: {AFFIRMATION}")
        user_input = input()

        if user_input != AFFIRMATION:
            print("That was not the affirmation.")

        elif user_input == AFFIRMATION:
            print("That's right! :)")
            break

if __name__ == "__main__":
    main()

