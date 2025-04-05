# Phonebook

## Problem Statement

In this program we show an example of using dictionaries to keep track of information in a phonebook.

## Solution Code

```python
def phonebook_data_store():

    phonebook_data = {}

    while True:
        name = input("Enter name: ")
        if name == "":
            break
        number = input("Enter number: ")

        phonebook_data[name] = number

    return phonebook_data

def print_phonebook(phonebook):
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")

def lookup(phonebook):

    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break

        if name not in phonebook:
            print(f"{name} is not in phonebook.")
        
        else:
            print(f"{name} -> {phonebook[name]}")


def main():
    phonebook = phonebook_data_store()
    print_phonebook(phonebook=phonebook)
    lookup(phonebook=phonebook)


if __name__ == "__main__":
    main()

