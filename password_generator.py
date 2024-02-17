import random

name = input("What's your name? ")

print(f"Hello {name}, Welcome to your Password Generator.")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,"

number = input("How many passwords do you need?: " )
number = int(number)

length = input("How many characters should your password be?: ")
length = int(length)

print("\nHere are your new passwords:")

for password in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)