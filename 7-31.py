# Define a function power(x, n) that calculates x^n. Apply recursion. Then, calculate 5^3.
# Tip: x^n = x * x^{n-1}

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print(power(5, 3))