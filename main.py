import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
cars = []
cars.append(CarManager())
player_1 = Player()
screen.onkey(player_1.move_player, 'Up')
sleep = 0.1
speed = 5

game_is_on = True
while game_is_on:
    time.sleep(sleep)
    screen.update()
    create_new_car = randint(1,20)

    # creates new cars randomly and puts them on the screen
    if create_new_car in [1, 0, 12, 15, 18]:
        cars.append(CarManager())

    # Moves current cars on the screen.
    for car in cars:
        car.set_car_speed(speed)
        car.move_car()

    # Detect if the player gets to the other side
    if player_1.detect_other_side():
        for c in cars:
            c.car_speed()
            speed = c.speed


    # Detect is player gets hit by a car
    for hit in cars:
        if hit.distance(player_1) < 20:
            game_is_on = False
            over = Scoreboard()
            over.game_over()

screen.exitonclick()