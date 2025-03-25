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