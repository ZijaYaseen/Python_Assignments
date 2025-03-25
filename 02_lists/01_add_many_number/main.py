def add_many_numbers(numbers):
    added_list : int = 0
    for number in numbers:
        added_list += number
    return added_list

def main():
    numbers = [1,2,3,4,5]
    sum = add_many_numbers(numbers)
    print(sum)

if __name__ == "__main__":
    main()


