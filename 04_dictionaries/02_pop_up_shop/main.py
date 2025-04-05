def main():
    fruits = {
        "apple" : 2,
        "mango" : 2,
        "banana" : 1,
        "kiwi" : 2,
        "strawberry" : 1
    }


    total_cost = 0
    for fruit_name in fruits:

        price = fruits[fruit_name]

        bought = int(input(f"How many {fruit_name} do you want to buy? "))

        total_cost += (price*bought)

    print(f"Your total is ${total_cost}")

if __name__ == "__main__":
    main()

         