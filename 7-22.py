# A text contains any number of words.
# Define a function f(name) that returns the acronym (first letters of all words).\
# Sample result:
# f("Internet of Things") returns "IoT"
# f("For Your Information") returns "FYI"
# f("Python") returns "P"

def f(name):
    acr = ""
    previous_space = True
    for ch in name:
        if ch == ' ':
            previous_space = True
        elif previous_space:
            acr += ch
            previous_space = False
    return acr

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))