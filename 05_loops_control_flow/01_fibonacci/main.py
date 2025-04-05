MAX_NUMBER = 10000

def main():

    current_num = 0
    next_num = 1

    while current_num <= MAX_NUMBER:
        print(current_num)
        after_next_num = current_num + next_num
        current_num = next_num
        next_num = after_next_num

if __name__ == "__main__":
    main()