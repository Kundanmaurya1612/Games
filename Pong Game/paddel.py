from turtle import Turtle

class Paddel(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.shapesize(3,1)
        self.setposition(position)
        # Movement Flags
        self.t1_up = False
        self.t2_up = False
        self.t1_down = False
        self.t2_down = False

    # Functions to set flags
    def t1_up_move_on(self): self.t1_up = True
    def t1_up_move_off(self): self.t1_up = False
    def t2_up_move_on(self): self.t2_up = True
    def t2_up_move_off(self): self.t2_up = False
    def t1_down_move_on(self): self.t1_down = True
    def t1_down_move_off(self): self.t1_down = False
    def t2_down_move_on(self): self.t2_down = True
    def t2_down_move_off(self): self.t2_down = False