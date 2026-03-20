from turtle import Turtle
from random import randint, choice

class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.seth(90)
        self.setpos(-70,-270)
        self.shape("turtle")
        self.color("yellow")
    def move(self):
        self.forward(7)
        

class Bots(Turtle):
    def __init__(self):
        super().__init__("square")
        self.paint_on_car = ["black",
                             "gray",
                             "silver",
                             "whitesmoke",
                             "rosybrown",
                             "firebrick",
                             "red",
                             "darksalmon",
                             "sienna",
                             "sandybrown",
                             "bisque",
                             "tan",
                             "moccasin",
                             "floralwhite",
                             "gold",
                             "darkkhaki"]
        self.color(choice(self.paint_on_car))
        self.penup()
        self.setpos(410, randint(-220,220))
        self.shapesize(1,2)
        self.seth(180)


class Lines(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.seth(180)
        self.pensize(2)
        self.setpos(position)
        self.pencolor("white")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.setpos(0,250)
        self.hideturtle()
        self.current_score = 1
        self.level()
    
    def level(self):
        self.write(f"Level: {self.current_score}",align="center", font=("Ariel", 30, "normal"))
    
    def increase(self):
        self.current_score += 1
        self.clear()
        self.level()

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        
    def over(self):
        self.write("Game Over",align="center", font=("Courier", 40, "bold"))
    