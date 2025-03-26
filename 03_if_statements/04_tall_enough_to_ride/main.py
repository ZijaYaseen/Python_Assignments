def main():

    MAX_HEIGHT = 50

    while True:
        input_height = input("How tall are you? (Write height in inches, e.g., if you are 6 feet, write 72): ")

        if not input_height:
            break

        try:
            height = int(input_height)

        except ValueError:
            print("Enter valid number")

        if height >= MAX_HEIGHT:
            print("You're tall enough to ride!")
            break
        else:
            print("You're not tall enough to ride!")

if __name__ == "__main__":
    main()        

