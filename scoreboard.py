from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "Center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(2, 2)
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 260)

    def display_score(self):
        self.clear()
        self.write(arg=f"{self.score}", move=FONT, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over", move=FONT, align=ALIGNMENT, font=FONT)


