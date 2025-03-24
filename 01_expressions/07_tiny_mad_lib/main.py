def main():
    print("Welcome to the Mad Libs game! Let's create a funny story.\nThis program prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!")

    adjective : str = input("Please type an adjective and press enter: ")
    noun : str = input("Please type an noun and press enter: ")
    verb : str = input("Please type an verb and press enter: ")

    # Funny sentence using the user's inputs
    print(f"Guess what? I just programmed Python to turn my {adjective} {noun} into a party animal that can {verb} all night long!")

if __name__ == "__main__":
    main()