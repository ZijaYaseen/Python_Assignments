# Shorten List

## Problem Statement
Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

## Solution Code

```python
MAX_LENGTH = 3

def shorten(lst):

    while len(lst) > MAX_LENGTH:
        lst.pop()
    print(lst)

def get_lst():
    
    lst = []
    elem = input("Enter a value: ")

    while elem != "":
        lst.append(elem)

        elem = input("Enter a value: ")

    return lst

def main():

    lst = get_lst()
    shorten(lst)

if __name__ == "__main__":
    main()