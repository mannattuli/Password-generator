import random
import array

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

UPLETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H''I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
  
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '~', '>', '*', '(', ')', '<']

pass1 = ''

for x in range(2):
    randomDigit = random. randint(0,9)
    pass1 = pass1 + DIGITS[randomDigit]

for i in range(3):
    randomUpletters = random. randint(0,25)
    pass1 = pass1 + UPLETTERS[randomUpletters]

for i in range(5):
    randomLetter = random. randint(0,25)
    pass1 = pass1 + LETTERS[randomLetter]

for x in range(2):
    randomChar = random. randint(0,14)
    pass1 = pass1 + SYMBOLS[randomChar]

print('A random password is:')
print(pass1)