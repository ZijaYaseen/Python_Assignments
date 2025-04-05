def main():
    counts = {}

    while True:
        num_input = input("\nEnter a value: ")

        if num_input == "":
            break

        try:
            num_input = int(num_input)

        except ValueError:
            print("Enter a valid number.")
            continue

        counts[num_input] = counts.get(num_input, 0) + 1

    for number , count in counts.items():
        print(f"\n{number} appers {count} times.")

if __name__ == "__main__":
    main()
