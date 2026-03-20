from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        self.number = -1
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.refresh()
        
    def refresh(self):
        self.clear()
        self.number += 1
        self.write(f"Score: {self.number}", align='center',font=("Courier", 14, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align='center',font=("Courier New", 20, "bold"))