from turtle import Turtle
from random import choice
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(1)
        self.speed(0)
        self.x_move = float(choice([-3,3]))
        self.y_move = float(choice([-3,3]))

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def restart(self) :
        self.reset()
        self.__init__()
        time.sleep(1)
        self.move()
        