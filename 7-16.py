# Define the function f(n), which returns the n-th value of the Fibonacci sequence. 
# The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. 
# Each subsequent value is the sum of the previous two. Sample result:
# f(5) returns 3
# f(9) returns 21

def f(n):
    previous = 0
    current = 1

    # -2 because we want the n-th step
    # but we already have F_0 and F_1 defined above
    # therefore before we even enter the loop
    # we are already 2 steps into the sequence
    for _ in range(n-2):
        temp = previous + current
        previous = current
        current = temp

    return current

print(f(5))
print(f(9))