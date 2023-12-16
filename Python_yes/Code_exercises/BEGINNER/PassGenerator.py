#module and create lists
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#start and inputs
print("Welcome to PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#src code
password = []
for i in range(nr_letters):
    pos_l = random.randint(0,len(letters)-1) 
    password.append(letters[pos_l])

for i in range(nr_symbols):
    pos_s = random.randint(0,len(symbols)-1) 
    password.append(symbols[pos_s])

for i in range(nr_numbers):
    pos_n = random.randint(0,len(numbers)-1) 
    password.append(numbers[pos_n])

random.shuffle(password)
password_str = ""
for i in password:
    password_str += i
print(f"Your password is: {password_str}")

