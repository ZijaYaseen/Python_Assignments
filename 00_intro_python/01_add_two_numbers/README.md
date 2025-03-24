# Add Two Numbers Program

## Problem Statement

Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

1. Prompt the user to enter the first number.
2. Read the input and convert it to an integer.
3. Prompt the user to enter the second number.
4. Read the input and convert it to an integer.
5. Calculate the sum of the two numbers.
6. Print the total sum with an appropriate message.

## Program Overview:

This program prompts the user to enter two numbers. It converts these inputs from strings to integers, calculates their sum, and then displays the result in a formatted message.

## Solution Code

```python
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
