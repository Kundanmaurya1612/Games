from turtle import Turtle

class Snake:
    def __init__(self):
        self.tims = []
        for i in range(3):
            self.tim = Turtle(shape="square")
            self.tim.color("white")
            self.tim.penup()
            self.tim.setposition(x=0-(i*20),y=0)
            self.tims.append(self.tim)
            
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.tims.append(new_segment)

    def extend(self):
        self.add_segment(self.tims[-1].position())

        
        

    def move(self):
        for snake in range(len(self.tims)-1, 0, -1):
            x = self.tims[snake-1].xcor()
            y = self.tims[snake-1].ycor()
            self.tims[snake].goto(x,y)
        self.tims[0].forward(20)

    def left(self):
        if self.tims[0].heading() == 0:
            pass
        else:
            self.tims[0].setheading(180)
    def right(self):
        if self.tims[0].heading() == 180:
            pass
        else:
            self.tims[0].setheading(0)
    def up(self):
        if self.tims[0].heading() == 270:
            pass
        else:
            self.tims[0].setheading(90)
    def down(self):
        if self.tims[0].heading() == 90:
            pass
        else:
            self.tims[0].setheading(270)