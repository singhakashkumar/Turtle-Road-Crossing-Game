import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    for kar in car.all_cars:
        if kar.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        if player.is_at_finish_line():
            player.goto_start()
            car.level_up()
            scoreboard.level_up()

screen.exitonclick()
