# Define a function f(text) that returns the given text with all characters separated by a dash sign. Example:
# f("Univesity") returns "U-n-i-v-e-r-s-i-t-y"
# f("UE") returns "U-E"
# f("x") returns "x"
# f("") returns ""

def f(text):
    fin = ""
    for i, ch in enumerate(text):
        if i != 0 and i < len(text):
            fin += '-'
        fin += ch
    return fin
    
print(f("Univesity"))
print(f("UE"))
print(f("x"))
print(f(""))