import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
turtle = Player()
car_manager = CarManager()
screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
def go_up():
    new_y = turtle.ycor() + 20
    turtle.goto(turtle.xcor(),new_y)

screen.listen()
screen.onkey(go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False
            scoreboard.game_over()

    if turtle.is_at_finish_line():
        turtle.go_to_start()
        car_manager.level_up()
        scoreboard.point()
screen.exitonclick()
