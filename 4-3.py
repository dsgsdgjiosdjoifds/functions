###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math

def triangle_area(a, b, c):
    s = 0.5 * (a + b + c)
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

print(f"The area of a triangle with sides {a}, {b}, {c} is {triangle_area(a, b, c):.0f}")