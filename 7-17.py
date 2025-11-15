# A palindrome is an expression that sounds the same when read backwards.
# Define a function f(palindrome) that returns True if the expression is a palindrome or False otherwise.
# Sample result:
# f("radar") returns True
# f("12-11-21") returns True
# f("book") returns False

def f(palindrome):
    for i, ch in enumerate(palindrome):
        # here we use -1 because in python
        # indexed iterators start from 0
        if ch != palindrome[-i-1]:
            return False
    return True

print(f("radar"))
print(f("12-11-21"))
print(f("book"))