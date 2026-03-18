from turtle import Turtle

class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.screenScore = 0
        self.setposition(position)
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(self.screenScore,align="center", font=("Ariel", 60, "normal")) 

    def increase(self):
        self.clear()
        self.screenScore += 1
        self.scoreboard() 
          
