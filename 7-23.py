# A valid password should consist of at least six characters and each character appears only once in the password.
# Define a function f(password) that returns True if the password is correct or False otherwise.
# Sample result:
# f("ax15") returns False
# f("book123") returns False
# f("A2water3") returns True
# f("qwerty") returns True
# f("") returns False

def f(password):
    chars = {}
    for ch in password:
        if chars.get(ch, False) == True:
            return False
        chars[ch] = True
    return len(chars) >= 6

print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))