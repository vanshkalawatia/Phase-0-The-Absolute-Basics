"""
Project: Password Generator
what it needs: random and string modules, loops
what it is: A script that generates a random password of a given length.

"""

import random, string

keys = string.ascii_letters + string.digits
try:
    length = int(input("Enter an given length for the password to be generated: "))

    password = ""
    for i in range (length):
        password += random.choice(keys)

    print(password)
except ValueError :
    print("Error: entered value is not an number.")
