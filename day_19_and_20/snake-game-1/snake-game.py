import time
from turtle import Screen
from snake import Snake
import sys

logo = """
          __
         {OO}
         \__/
          |^|              SNAKE  GAME              /|
          | |______________________________________/ /
          \_________________________________________/                                                                                
"""


def print_usage():
    print("Usage: python snake-game.py [game_mode]")
    print("       - game mode: easy, normal, hard")
    print("       - default game mode: normal")


print(logo)
print("Welcome to Snake Game!")
print("Please use arrow keys to control the snake.\n")
print_usage()

# default mode: normal
speed = 0.5

if len(sys.argv) > 2:
    print("Invalid game mode. Please select available game mode.")
    sys.exit(1)

if len(sys.argv) == 2:
    game_mode = sys.argv[1].lower()
    if game_mode == "easy":
        speed = 1
    elif game_mode == "normal":
        speed = 0.5
    elif game_mode == "hard":
        speed = 0.3
    else:
        print("Invalid game mode. Please select available game mode.")
        sys.exit(1)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()


