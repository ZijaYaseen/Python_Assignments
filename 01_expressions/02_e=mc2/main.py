C : int = 299792458

def main():
    mass_in_kgs = float(input("Enter kilos of mass: "))

    energy_of_joules : float = mass_in_kgs * (C ** 2)

    print("e = m * C^2...")
    print(f"m = {mass_in_kgs}kg")
    print(f"c = {C} m/s")
    print(f"{energy_of_joules} joules of energy!")

if __name__ == "__main__":
    main()