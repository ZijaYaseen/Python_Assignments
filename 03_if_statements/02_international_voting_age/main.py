PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    age: int = int(input("How old are you? "))

    if age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is 16.") 
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is 16.")

    if age >= STANLAU_AGE:

        print(f"You can vote in Stanlau where the voting age is 25.") 
    else:
        print(f"You cannot vote in Stanlau where the voting age is 25.")

    if age >= MAYENGUA_AGE:

        print(f"You can vote in Mayengua where the voting age is 48.") 
    else:
        print(f"You cannot vote in Mayengua where the voting age is 48.")

if __name__ == "__main__":
    main()