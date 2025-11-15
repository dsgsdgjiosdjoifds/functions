# Define a function f(n) that returns a string of n asterisks, separated by a slash sign. Sample result:
# f(4) returns "*/*/*/*"
# f(1) returns "*"

def f(n):
    ret = ""
    for i in range(n):
        if i != 0 and i < n:
            ret += '/'
        ret += '*'
    return ret

print(f(4))
print(f(1))