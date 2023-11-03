from turtle import Turtle
from random import Random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
random = Random()



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.goto(280, random.randint(-240, 240))
        self.setheading(180)
        self.showturtle()
        self.speed = STARTING_MOVE_DISTANCE

    def move_car(self):
        self.forward(self.speed)

    def car_speed(self):
        self.speed += MOVE_INCREMENT

    def set_car_speed(self, speed):
        self.speed = speed


