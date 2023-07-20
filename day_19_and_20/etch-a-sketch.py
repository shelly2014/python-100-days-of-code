from turtle import *

# initialization
tim = Turtle()
tim.pensize(1)
tim.speed(10)
screen = Screen()
key_states = {"Right": False, "Left": False, "Up": False, "Down": False}


def move_forwards(heading_val):
    tim.setheading(heading_val)
    tim.forward(10)
    clear_key_states()


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def set_key_states(key, state):
    key_states[key] = state
    check_key_states()


def clear_key_states():
    for key in key_states:
        key_states[key] = False


def check_key_states():
    if key_states["Right"] and key_states["Up"]:
        move_forwards(45)
    elif key_states["Right"] and key_states["Down"]:
        move_forwards(315)
    elif key_states["Left"] and key_states["Up"]:
        move_forwards(135)
    elif key_states["Left"] and key_states["Down"]:
        move_forwards(225)
    elif key_states["Right"]:
        move_forwards(0)
    elif key_states["Left"]:
        move_forwards(180)
    elif key_states["Up"]:
        move_forwards(90)
    elif key_states["Down"]:
        move_forwards(270)


LOGO = """
      _       _                   _        _       _     
  ___| |_ ___| |__     __ _   ___| | _____| |_ ___| |__  
 / _ \ __/ __| '_ \   / _` | / __| |/ / _ \ __/ __| '_ \ 
|  __/ || (__| | | | | (_| | \__ \   <  __/ || (__| | | |
 \___|\__\___|_| |_|  \__,_| |___/_|\_\___|\__\___|_| |_|
"""
print(LOGO)
print("""
Welcome to Etch-a-Sketch Game!

* up arrow key             move upwards
* down arrow key           move downwards
* left arrow key           move left
* right arrow key          move right
* up + right arrow key     move top-right corner
* up + left arrow key      move top-left corner
* down + right arrow key   move bottom-right corner
* down + left arrow key    move bottom-left corner 
* space key                clear

Get creative! Experiment with different movements and combinations of arrow keys!     

Have fun and happy drawing!
""")


screen.listen()
screen.title("Etch-a-Sketch")
screen.onkey(lambda: set_key_states("Right", True), "Right")
screen.onkey(lambda: set_key_states("Left", True), "Left")
screen.onkey(lambda: set_key_states("Up", True), "Up")
screen.onkey(lambda: set_key_states("Down", True), "Down")
screen.onkey(key="space", fun=clear)

screen.exitonclick()
