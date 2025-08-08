import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

str=""
newStr=""

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for i in range(1,nr_letters+1):
    str+=random.choice(letters)

for i in range(1,nr_symbols+1):
    str+=random.choice(symbols)

for i in range(1,nr_numbers+1):
    str+=random.choice(numbers)
    
print(f"The Current Easy level Password generated is {str}")
    
pList=[]

for char in str:
    pList.append(char)

random.shuffle(pList)

for el in pList:
    newStr+=el
    
print(f"The Hard Password generated is {newStr}")