from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-290, 260)
        self.hideturtle()
        self.draw()

    def draw(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update(self):
        self.level += 1
        self.draw()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)