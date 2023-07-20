import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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
    print("Usage: python main.py [game_mode]")
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
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
game_is_on = True


def restart_or_exit():
    global game_is_on
    scoreboard.game_over()
    user_choice = screen.textinput("Restart or Exit", "Enter 'y' to restart the game, or any other key to exit.")
    if user_choice.lower() == "y":
        scoreboard.restart()
        snake.restart()
        screen.listen()
    else:
        game_is_on = False
        return


while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        restart_or_exit()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            restart_or_exit()

screen.exitonclick()
