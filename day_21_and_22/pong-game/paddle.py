from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position, color, screen_height):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.max_ycor = screen_height/2 - 50
        self.min_ycor = -1 * screen_height/2 + 50

    def go_up(self):
        new_y = self.ycor() + 20
        if self.min_ycor <= new_y <= self.max_ycor:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if self.min_ycor <= new_y <= self.max_ycor:
            self.goto(self.xcor(), new_y)
