def main():
    print("This program will divide two numbers and show the quotient and remainder.")

    divided : int = int(input("Please enter an integer to be divided: "))
    divided_by : int = int(input("Please enter an integer to divide by: "))

    quotient = divided // divided_by # ye divide ho rha he // is liye qk foat me na ye numbers answers
    remainder = divided % divided_by # ye remainder k liye 

    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    main()