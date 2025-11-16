# Define the function f(x,y), which returns the sum of numbers in the range <x,y> that are completely 
# divisible by 2 and 3 and not divisible by 4. Sample result:
# f(1,20) returns 24
# f(10,30) returns 48

def f(x, y):
    _sum = 0
    for i in range(x, y+1):
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
            _sum += i
    return _sum

print(f(1,20))
print(f(10,30))