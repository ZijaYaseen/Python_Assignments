def phonebook_data():

    phonebook = {}

    while True:
        name = input("Enter name: ")
        if name == "":
            break

        number = input("Enter number: ")

        phonebook[name] = number
    return phonebook

def print_phonebook(phonebook):

    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")

def lookup(phonebook):

    while True:
        name = input("Enter name: ")
        if name == "":
            break

        if name not in phonebook:
            print(f"{name} not in phonebook.")

        else:
            print(f"{name} -> {phonebook[name]}")

def main():
    phonebook = phonebook_data()
    print_phonebook(phonebook)
    lookup(phonebook)

if __name__ == "__main__":
    main()


