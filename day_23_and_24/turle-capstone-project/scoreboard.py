from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, attempts_total):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard(attempts_total)

    def update_scoreboard(self, attempts_left):
        self.clear()
        self.goto(-280, 250)
        self.color("green")
        self.write("Level: " + str(self.level), align="left", font=FONT)
        self.goto(280, 250)
        self.write('❤ ' * attempts_left, align="right", font=FONT)

    def upgrade_level(self, attempts_left):
        self.level += 1
        self.update_scoreboard(attempts_left)

    def game_over(self):
        self.update_scoreboard(0)
        self.goto(0, 100)
        self.write("GAME OVER", align="center", font=FONT)
