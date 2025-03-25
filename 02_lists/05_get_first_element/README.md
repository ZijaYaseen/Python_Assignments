# Get First Element

## Problem Statement
Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

## Solution Code

```python
def get_first_element(lst):
    print(lst[0])

def list_of_elements():

    lst = []
    elements = input("Please enter an element of the list or press enter to stop. ")

    while elements != "":
        lst.append(elements)
        elements = input("Please enter an element of the list or press blank enter to stop. ")
        lst.append(elements)

    return lst

def main():
    lst = list_of_elements()
    get_first_element(lst)

if __name__ == "__main__":
    main()
