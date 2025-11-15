def draw_square(length):
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(length):
    pen.right(60)
    pen.forward(length)
    for _ in range(2):
        pen.right(120)
        pen.forward(length)
    pen.right(60) # to reset the turtle's rotation

def draw_rectangle(a, b):
    for _ in range(2):
        pen.forward(a)
        pen.right(90)
        pen.forward(b)
        pen.right(90)