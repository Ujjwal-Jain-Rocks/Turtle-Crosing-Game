import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.turtles = []
        self.increase_speed = 0
        for _ in range(30):
            turtle = Turtle("square")
            turtle.shapesize(stretch_len=2, stretch_wid=1)
            turtle.penup()
            turtle.setheading(180)
            turtle.color(random.choice(COLORS))
            turtle.goto(random.randint(-300, 300), random.randint(-260, 260))
            self.turtles.append(turtle)

    def update(self):
        for turtle in self.turtles:
            turtle.forward(STARTING_MOVE_DISTANCE + self.increase_speed)
            if turtle.xcor() < -300:
                turtle.goto(300, turtle.ycor())

    def new_level(self):
        self.increase_speed += MOVE_INCREMENT
        print(self.increase_speed)