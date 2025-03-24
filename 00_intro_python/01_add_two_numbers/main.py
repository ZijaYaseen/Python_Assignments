def main():
    print('This program adds two numbers\n')
    num1 : str = input("Enter first number: ")
    num1 : int = int(num1)

    num2 : str = input("Enter second number: ")
    num2 : int = int(num2)

    total = num1 + num2

    print(f"The total is: {total}")

if __name__ == '__main__':
    main()
