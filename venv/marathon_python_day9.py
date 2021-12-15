## project: password generator

# import random module
import random

# define characters used in password
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["~", "!", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# input password combination
print("Password Generator")
num_numbers = int(input("How many numbers would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_letters = int(input("How many letters would you like in your password?\n"))

# randomly choose characters
password_list = []

for number in range(1, num_numbers + 1):
    password_list += random.choice(numbers)

for symbol in range(1, num_symbols + 1):
    password_list += random.choice(symbols)

for letter in range(1, num_letters + 1):
    password_list += random.choice(letters)

# shuffle the password_list
random.shuffle(password_list)

# turn the password list into string
password = ""
for password_char in password_list:
    password += password_char
print(password)
