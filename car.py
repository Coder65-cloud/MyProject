from turtle import Turtle
import random
import time

position = [210, 170, 130, 90, 50, 10, -30, -70, -110, -150, -190, -220]
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(self.rand_color())
        self.penup()
        self.shape("square")
        self.speed(1)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(320, 210)
        self.step = 0

    def rand_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rand_c = (r, g, b)
        return rand_c

    def starting_position(self, index):
        x = self.xcor()
        y = position[index]
        self.goto(x, y)

    def rand_step(self):
        rand_move = random.randint(10, 20)
        return rand_move

    def move_car(self):
        rand_step = self.rand_step()
        new_x = self.xcor() - rand_step
        self.goto(new_x, self.ycor())

    def collision_wall(self, index):
        if self.xcor() < -300:
            self.goto(320, 210)
            self.starting_position(index)
