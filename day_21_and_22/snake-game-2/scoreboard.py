from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Current Score: {self.score} | Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.clear()
        self.update_scoreboard()
        self.goto(0, 100)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def restart(self):
        self.clear()
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
