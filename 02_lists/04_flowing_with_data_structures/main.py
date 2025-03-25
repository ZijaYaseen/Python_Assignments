def add_three_copies(my_list, message):
    for i in range(3):
        my_list.append(message)
        
def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print(f"Before List: {my_list}")
    add_three_copies(my_list, message)
    print(f"After List: {my_list}")

if __name__ == "__main__":
    main()
