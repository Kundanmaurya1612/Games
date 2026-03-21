from turtle import Turtle
import os

class Score(Turtle):

    def __init__(self):
        self.current_score = 0
        self.high_score = 0
        self.file_path = os.path.join('Snake Game', 'data.txt')
        with open(self.file_path) as f:
            self.high_score = int(f.read())
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.write(f"Score:{self.current_score} High Score:{self.high_score}", align='center',font=("Courier", 14, "normal"))
        
    def update(self):
        self.clear()
        self.write(f"Score:{self.current_score} High Score:{self.high_score}", align='center',font=("Courier", 14, "normal"))

    def refresh(self):
        if self.current_score > self.high_score:
            with open(self.file_path, "w") as f:
                f.write(str(self.current_score))
            self.high_score = self.current_score
            self.current_score = 0
            self.update()
        else:
            self.current_score = 0
            self.update()