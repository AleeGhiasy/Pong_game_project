from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.speed = 0.1

    def move_ball(self):
        x= self.xcor() + self.xmove
        y= self.ycor() + self.ymove
        self.goto(x,y)

    def y_bounce(self):
        self.ymove *= -1

    def x_bounce(self):
        self.xmove *= -1
        self.speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.x_bounce()
        self.speed = 0.1
