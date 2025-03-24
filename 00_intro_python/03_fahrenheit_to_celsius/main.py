def main():
    print("This program converts Fahrenheit temperature into Celcius.")

    degrees_fahrenheit : float = float(input("Enter temperature in Fahrenheit: "))

    degrees_celcius = (degrees_fahrenheit - 32) * 5.0/9.0

    print(f'Temperature: {degrees_fahrenheit:.1f}F = {degrees_celcius}C')

if __name__ == '__main__':
    main()


