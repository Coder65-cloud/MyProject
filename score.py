from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.n = 0
        self.dashboard()
        self.speed_time = 0.1

    def dashboard(self):
        self.goto(x=-240,y=250)
        self.write(arg="Level:", align="center", font=("Courier New", 22, "normal"))
        self.goto(x=-180, y=250)
        self.write(arg=self.n, align="center", font=("Courier New", 22, "normal"))

    def increase_score(self):
        self.n += 1
        self.clear()
        self.dashboard()

    def collision_car(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Courier New", 22, "normal"))

    def increase_speed(self):
        self.speed_time *= 0.5
