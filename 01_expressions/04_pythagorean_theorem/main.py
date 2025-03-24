import math

def main():
    print("This program calculates the hypotenuse of a right triangle using the Pythagorean theorem.")

    AB : float = float(input("Enter the length of AB: "))
    AC : float = float(input("Enter the length of Ac: "))

    BC : float = math.sqrt((AB ** 2) + (AC ** 2))

    print(f"The length of BC (the hypotenuse) is: {BC}")

if __name__ == "__main__":
    main()