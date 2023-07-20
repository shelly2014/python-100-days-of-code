from turtle import Turtle
import random

COLORS = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            hex_color = '#%02x%02x%02x' % random.choice(COLORS)
            new_car.color(hex_color)
            random_y = self.get_random_y()
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def get_random_y(self):
        while 1:
            overlap = False
            random_y = random.randint(-250, 250)
            for car in self.all_cars:
                # Check if the new car overlaps with existing cars close to the starting lane
                if car.xcor() > 260 and car.ycor() + 20 > random_y > car.ycor() - 20:
                    overlap = True
                    break

            if not overlap:
                break

        return random_y

    def move_cars(self):
        for car in self.all_cars[:]:
            car.backward(self.car_speed)
            # Delete from the car array when car moves out of the screen
            if car.xcor() < -320:
                self.all_cars.remove(car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
