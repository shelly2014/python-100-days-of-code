from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, attempts_total):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.y_move = MOVE_DISTANCE
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.attempts_left = attempts_total

    def go_up(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def decrease_attempts(self):
        self.attempts_left -= 1

    def no_attempts_lef(self):
        return self.attempts_left <= 0
