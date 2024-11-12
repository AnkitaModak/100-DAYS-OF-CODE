from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
ball = Ball()
scoreboard = Scoreboard()
screen = Screen()
screen.bgcolor("Black")
screen.title("The Pong Game")
screen.setup(height = 600 , width = 800)
screen.tracer(0)
screen.listen()
r_paddle = Paddle((380,0))
l_paddle = Paddle((-380,0))
def go_up():
    new_y = r_paddle.ycor() + 20
    r_paddle.goto(r_paddle.xcor(), new_y)
def go_down():
    new_y = r_paddle.ycor() - 20
    r_paddle.goto(r_paddle.xcor(), new_y)
screen.onkey(go_up,"Up")
screen.onkey(go_down, "Down")
def move_up():
    new_y = l_paddle.ycor() + 20
    l_paddle.goto(l_paddle.xcor(), new_y)
def move_down():
    new_y = l_paddle.ycor() - 20
    l_paddle.goto(l_paddle.xcor(), new_y)
screen.onkey(move_up,"w")
screen.onkey(move_down, "s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if  ball.distance(r_paddle) < 50 and ball.xcor() > 350 or  ball.distance(l_paddle) < 50 and ball.xcor() > -360:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
