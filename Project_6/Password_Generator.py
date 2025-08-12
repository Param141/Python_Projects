import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - This would give letters,symbols and numbers not in random order 
# random.choice() gives random index element from the list  
# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(password)

# Hard level
password_list = [] #add each of character in list instead of strings but would be stored as a string only with single qoutations 
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
    # or could have used password_list += random.choice(letters) also it would also work 

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list) # using shuffle function to suffle the list by random.shuffle(x )
print(password_list) # random list now so convert back to  string using for loop 

# This would give letters,symbols and numbers in random order 

password = ""
for char in password_list:  
    password += char

print(f"Your password is: {password}")

# to generate numbers from 1 to n will do range(1,n+1) ie. user wants 4 letters in password
# then would use range(1,5)
# or to generate n numbers starting from 0 will do range(0,n)