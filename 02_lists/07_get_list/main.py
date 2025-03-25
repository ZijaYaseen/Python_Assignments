def get_lst():
    lst = []
    elements = input("Please enter an element of the list or press enter to stop. ")

    while elements != "":
        lst.append(elements)
        elements = input("Please enter an element of the list or press blank enter to stop. ")

    return lst

def main():
    lst= get_lst()
    print(f"Here's the list: {lst}")

if __name__ == "__main__":
    main()