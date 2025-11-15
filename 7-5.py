from in_range import is_in_range

x = 2
y = 15

number = int(input("A number: "))
print(f"Number {number} in the range <{x},{y}>: {"yes" if is_in_range(number, x, y) else "no"}")