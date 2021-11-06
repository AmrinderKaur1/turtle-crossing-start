from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X = [-300, 300]
Y_AXES_LIST = [[120, 220], [20, 120], [-120, -20], [-220, -120]]


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_colors(self):
        clr = random.choice(COLORS)
        return clr

    def create_car(self):
        head = 0
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            random_y_axis = random.choice(Y_AXES_LIST)
            y = random.randint(random_y_axis[0], random_y_axis[1])
            if y > 0:
                x_axis = X[1]
                head = 180
            elif y < 0:
                x_axis = X[0]

            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car_color = self.car_colors()
            new_car.color(new_car_color)
            new_car.goto(x_axis, y)
            new_car.setheading(head)
            self.all_cars.append(new_car)

            new_t1 = Turtle(shape="circle")
            new_t1.shapesize(stretch_wid=0.5, stretch_len=0.5)
            new_t1.penup()
            new_t1.color("black")
            y_cor1 = y - 10
            new_t1.goto(x_axis - 10, y_cor1)
            new_t1.setheading(head)
            self.all_cars.append(new_t1)

            new_t2 = Turtle(shape="circle")
            new_t2.shapesize(stretch_wid=0.5, stretch_len=0.5)
            new_t2.penup()
            new_t2.color("black")
            new_t2.goto(x_axis + 10, y_cor1)
            new_t2.setheading(head)
            self.all_cars.append(new_t2)

    def move_cars(self):
        for i in range(0, len(self.all_cars), 3):
            self.all_cars[i].forward(self.car_speed)
            self.all_cars[i+1].forward(self.car_speed)
            self.all_cars[i+2].forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
