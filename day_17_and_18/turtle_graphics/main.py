import turtle as t
import random
import time

tim = t.Turtle()
t.colormode(255)
tim.pensize(5)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_square_spirograph(size, size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)
        for _ in range(4):
            tim.forward(size)
            tim.right(90)


def draw_spirograph(size, size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(size)
        tim.setheading(tim.heading() + size_of_gap)


# draw_spirograph(100, 5)
draw_square_spirograph(100, 5)

screen = t.Screen()
screen.exitonclick()
