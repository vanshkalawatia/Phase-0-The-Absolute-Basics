"""
Project: Temperature Converter

What it needs: Functions, float(), arithmetic, error handling

What it is: A script that converts Celsius to Fahrenheit and vice versa.
"""

conversion = input("Enter the ( '0' for Celsius to Fahrenheit) and ( '1' for Fahrenheit to Celsius ): ")

if conversion == "0":
    try:
        degree = float(input("Enter the 'Celsius' to be converted: "))
        fahrenheit = (degree * 1.8) + 32
        print(f"{degree} Celsius is {fahrenheit} Fahrenheit")

    except ValueError:
        print("Error: It was not an valid number.")

elif conversion == "1":
    try:
        fahrenheit = float(input("Enter the 'Fahrenheit' to be converted: "))
        degree = (fahrenheit -32) * 0.56
        print(f"{degree} Celsius is {fahrenheit} Fahrenheit")

    except ValueError:
        print("Error: It was not an valid number.")
else:
    print("Enter an valid input.")
