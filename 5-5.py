import turtle
from figures import draw_square, draw_rectangle, draw_triangle

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

def move_turtle(forward, row):
    pen.penup()
    pen.goto(100 if forward else -100, 400 - 150 * row)
    pen.pendown()

# draw each figure twice
move_turtle(False, 1)
draw_square(100)
move_turtle(True, 1)
draw_square(50)

move_turtle(False, 2)
draw_triangle(150)
move_turtle(True, 2)
draw_triangle(75)

move_turtle(False, 3)
draw_rectangle(20, 50)
move_turtle(True, 3)
draw_rectangle(100, 30)

pen.hideturtle()
window.mainloop()