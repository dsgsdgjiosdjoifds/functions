# Define the function f(number1,number2,number3), which returns the difference between the largest and smallest numbers. 
# Sample result:
# f(7,4,9) returns 5
# f(2,12,8) returns 10

def f(n1, n2, n3):
    _min = min(n1, n2, n3)
    _max = max(n1, n2, n3)
    return _max - _min

print(f(7,4,9))
print(f(2,12,8))