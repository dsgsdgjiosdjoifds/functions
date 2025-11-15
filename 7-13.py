# Define the function f(n), which returns numbers from 1 to n as a string. Sample result:
# f(11) returns "1234567891011"
# f(4) returns "1234"

def f(n):
    text = ""
    for i in range(n+1):
        text += str(i)
    return text

print(f(11))
print(f(4))