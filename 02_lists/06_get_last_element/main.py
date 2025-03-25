def get_last_element(lst):
    print(lst[-1])

def list_of_elements():

    lst = []
    elements = input("Please enter an element of the list or press enter to stop. ")

    while elements != "":
        lst.append(elements)
        elements = input("Please enter an element of the list or press blank enter to stop. ")

    return lst

def main():
    lst = list_of_elements()
    get_last_element(lst)

if __name__ == "__main__":
    main()
