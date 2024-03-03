import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
screen = Screen()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")
screen.listen()
screen.onkey(player.move, "5")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    for car in car_manager.cars:
        if player.distance(car) <= 20:
            scoreboard.game_over()
            game_is_on = False
    if player.successful_cross():
        player.go_to_starting_point()
        car_manager.increase_speed()
        scoreboard.increase_score()
screen.exitonclick()