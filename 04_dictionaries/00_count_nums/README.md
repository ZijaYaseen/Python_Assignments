# Leap Year

## Problem Statement

This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

## Solution Code

```python
def main():
    counts = {}

    while True:
        num_input = input("\nEnter a value: ")

        if num_input == "":
            break

        try:
            num_input = int(num_input)

        except ValueError:
            print("Enter a valid number.")
            continue

        counts[num_input] = counts.get(num_input, 0) + 1

    for number , count in counts.items():
        print(f"\n{number} appers {count} times.")

if __name__ == "__main__":
    main()

