from turtle import Turtle

LANE_LIST_DARK = [240, -240]
LANE_LIST_DASHED = [120, -120]
X = 300


class Road:

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.pensize(3)
        self.turtle.goto(X, 0)
        self.turtle.pendown()
        self.turtle.backward(600)
        self.draw_lanes()
        self.draw_crossing()

    def draw_lanes(self):

        for i in LANE_LIST_DARK:
            self.turtle.penup()
            self.turtle.goto(X, i)
            self.turtle.pendown()
            self.turtle.pensize(4)
            self.turtle.backward(600)

        for j in LANE_LIST_DASHED:
            self.turtle.penup()
            x = X
            self.turtle.goto(X, j)
            self.turtle.pensize(2)
            while x != -300:
                self.turtle.pendown()
                self.turtle.backward(20)
                self.turtle.penup()
                self.turtle.backward(10)
                x -= 30

    def draw_crossing(self):
        self.turtle.penup()
        self.turtle.pensize(5)
        self.turtle.goto(-40, -220)
        self.turtle.pendown()
        self.turtle.pensize(5)

        for i in range(0, 22):
            if i == 22:
                self.turtle.pensize(0)
            else:
                self.turtle.pensize(5)
            self.turtle.setheading(0)
            self.turtle.forward(80)
            self.turtle.penup()
            self.turtle.setheading(90)
            self.turtle.forward(20)
            self.turtle.setheading(180)
            self.turtle.pendown()
            self.turtle.forward(80)

        self.turtle.hideturtle()






