from turtle import Turtle, Screen
from car import Car
from player import Player
from score import Score
import time
import random
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.colormode(255)

# Player code
player = Player()
screen.listen()
screen.onkey(key="Up", fun=player.move)

# Dashboard
score = Score()

# Cars generator
cars_group = []
for num in range(12):
    car = Car()
    car.starting_position(num)
    cars_group.append(car)



# Game Loop
game_is_on = True
index = 0
while game_is_on:
    time.sleep(score.speed_time)
    for car_object in cars_group:
        rand_car = random.choice(cars_group)
        rand_car.move_car()
        screen.update()
        rand_car.collision_wall(index)
        index += 1
        if index == 11:
            index = 0
        if player.collision_with_wall():
            score.increase_score()
            score.increase_speed()
        if rand_car.distance(player) < 20:
            score.collision_car()
            game_is_on = False



screen.exitonclick()