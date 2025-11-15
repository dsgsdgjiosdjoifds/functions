# Define the function f(n1,n2,n3), which returns True if at least one of the numbers n1,n2,n3 is negative or False otherwise.
# f(11,6,-4) returns True
# f(5,4,14) returns False

def f(n1, n2, n3):
    return n1 < 0 or n2 < 0 or n3 < 0

print(f(11, 6, -4))
print(f(5, 6, 14))