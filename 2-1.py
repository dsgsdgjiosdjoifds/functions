###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input("Letter: ")
print(f'Letter from the keyboard: {letter[0]}')

number = int("20303")
print(f'Number representing the string: {number}')

binary = bin(304)
print(f'Binary string representing number 304: {binary}')

hexadecimal = hex(304)
print(f'Hexadecimal string representing number 304: {hexadecimal}')

uni = ord('€')
print(f"€ sign is represented by unicode code: {uni}")

absolute = abs(-17)
print(f'Absolute value of -17: {absolute}')