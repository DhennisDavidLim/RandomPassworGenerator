import random
#Password Generator Project

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

tempLetter = []
for letter in range(nr_letters):
  ranLetters = random.choice(letters)
  tempLetter.append(ranLetters)

for number in range(nr_numbers):
  ranNumbers = random.choice(numbers)
  tempLetter.append(ranNumbers)

for symbol in range(nr_symbols):
  ranSymbols = random.choice(symbols)
  tempLetter.append(ranSymbols)

random.shuffle(tempLetter)
combineString = ''.join(map(str, tempLetter))
print(f"This is Your Random Generator Password {combineString}")
  






  


  