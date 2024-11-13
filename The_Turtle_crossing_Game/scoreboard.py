from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-230, 250)
        self.Level = 1
        self.update()
    def update(self):
        self.clear()
        self.write(f"Level:{self.Level}", align="center", font=FONT)
    def point(self):
        self.Level += 1
        self.update()
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)



