from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(x=0, y=-250)
        self.boundary = 0

    def move(self):
        self.forward(20)

    def collision_with_wall(self):
        if self.ycor() > 300:
            self.goto(x=0, y=-250)
            return True
