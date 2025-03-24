# Remainder Division

## Problem Statement

Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

Here's a sample run of the program (user input is in bold italics):

Please enter an integer to be divided: 5

Please enter an integer to divide by: 3

The result of this division is 1 with a remainder of 2

## Solution Code

```python
def main():
    print("This program will divide two numbers and show the quotient and remainder.")

    divided : int = int(input("Please enter an integer to be divided: "))
    divided_by : int = int(input("Please enter an integer to divide by: "))

    quotient = divided // divided_by # ye divide ho rha he // is liye qk float me na aye numbers answers
    remainder = divided % divided_by # ye remainder k liye 

    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    main()