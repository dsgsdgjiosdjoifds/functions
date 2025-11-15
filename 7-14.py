# Two numbers and an operator are given.
# Define a function f(number1,number2,operator) that returns the result of an arithmetic operation.
# The available operators are +,-,*,%,**.
# Sample result:
# f(2,3, "+") returns 5
# f(2,3, "%") returns 2
# f(2,3, "**") returns 8
# f(2,3, "*") returns 6
# f(2,3, "-") returns -1

def f(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '%':
        return n1 % n2
    elif op == '**':
        return n1 ** n2
    elif op == '*':
        return n1 * n2
    elif op == '-':
        return n1 - n2
    
print(f(2,3, "+"))
print(f(2,3, "%"))
print(f(2,3, "**"))
print(f(2,3, "*"))
print(f(2,3, "-"))