from turtle import Screen
import time

class SnakeScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("#1F1F1F")
        self.screen.title("My snake game🐍")


        self.screen.setup(600,600)
        self.screen.tracer(0)
    
    def update(self):
        self.screen.update()
        time.sleep(0.2)

    