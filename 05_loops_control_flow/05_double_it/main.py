def main():
    try:
        current_value = int(input("Enter number to double it: "))

        current_value = current_value * 2

        while current_value < 100:
            print(current_value, end=' ')
            current_value = current_value * 2

        print(current_value)

    except ValueError:
        print("Invalid syntax. Enter a valid number.")
        

if __name__ == "__main__":
    main()
