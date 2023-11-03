from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.scoreboard = Scoreboard()
        self.scoreboard.display_score()

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def detect_other_side(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.scoreboard.update_score()
            return True
        return False
