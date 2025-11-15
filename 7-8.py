# The vending machine accepts 1, 2 and 5 PLN coins.
# Define a function f(amount_to_pay) that returns the minimum number of coins that can 
# be used to pay for the purchased product.
# Sample result:
# f(23) returns 6
# f(8) returns 3
# f(2) returns 1
# f(0) returns 0

def f(amount):
    coins = amount // 5
    amount -= coins * 5
    coins += amount // 2
    amount -= (amount // 2) * 2
    coins += amount
    return coins

print(f(23))
print(f(8))
print(f(2))
print(f(0))