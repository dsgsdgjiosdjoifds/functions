# The sequence of digits contains the number of points rolled with a dice.
# Define a function f(dice) that returns a number specifying the number of dice rolled the most times in a row.
# Sample result:
# f("5233165554211") returns 5
# f("2133") returns 3

def f(dice):
    numbers = {}
    for ch in dice:
        digit = int(ch)
        count = numbers.get(ch, 0)
        numbers[ch] = count + 1
    most = numbers.get(0)
    biggest = 0
    for k,v in numbers.items():
        if v > biggest:
            biggest = v
            most = int(k)
    return most

print(f("5233165554211"))
print(f("2133"))