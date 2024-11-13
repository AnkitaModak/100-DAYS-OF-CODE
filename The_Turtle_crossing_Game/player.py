from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("pink")
        self.shape("turtle")
        self.speed("fastest")
        self.penup()
        self.go_to_start()
        self.left(90)
    def go_to_start(self):
        self.goto(STARTING_POSITION)
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


