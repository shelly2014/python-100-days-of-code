import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

ATTEMPTS_TOTAL = 3

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Road Game")
screen.tracer(0)

player = Player(ATTEMPTS_TOTAL)
car_manager = CarManager()
scoreboard = Scoreboard(ATTEMPTS_TOTAL)

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            player.decrease_attempts()
            if player.no_attempts_lef():
                game_is_on = False
                scoreboard.game_over()
            else:
                player.go_to_start()
                scoreboard.update_scoreboard(player.attempts_left)

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.upgrade_level(player.attempts_left)

screen.exitonclick()
