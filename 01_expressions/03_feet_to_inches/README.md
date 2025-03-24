# Feet To Inches 

## Problem Statement

Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

## Code Solution

```python
inches_in_feet = 12

def main():
    feet : float = float(input("Enter number in feet: "))

    inches = feet * inches_in_feet 

    print(f"That is {inches:.1f} inches.")

if __name__ == "__main__":
    main()
