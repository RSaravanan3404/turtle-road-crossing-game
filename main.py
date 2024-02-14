import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from divider import Divider

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
score = Scoreboard()
car = CarManager()
divider = Divider()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car_at_lane1()
    car.create_car_at_lane2()
    car.move_cars()
    for one_car in car.lane1_cars:
        if player.distance(one_car) < 20 and player.xcor() < one_car.xcor():
            game_is_on = False
            score.game_over()
    for one_car in car.lane2_cars:
        if player.distance(one_car) < 20 and player.xcor() > one_car.xcor():
            game_is_on = False
            score.game_over()
    if player.is_at_line():
        player.go_to_start()
        car.level_up()
        score.update_level()

screen.exitonclick()
