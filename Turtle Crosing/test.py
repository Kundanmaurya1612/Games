from turtle import Turtle, Screen
import random

class Enemy(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.color("red")
        self.setposition(300, random.randint(-250, 250))
        self.speed("fastest")

    def move(self):
        self.setx(self.xcor() - 10) # Move left

# Setup
screen = Screen()
enemies = []

def game_loop():
    # Spawn new enemy occasionally
    if random.randint(1, 5) == 1:
        enemies.append(Enemy())
    
    # Move all enemies
    for enemy in enemies:
        enemy.move()
        
    screen.update()
    screen.ontimer(game_loop, 100) # Loop every 100ms

screen.tracer(0) # Turns off animation for faster spawning/movement
game_loop()
screen.exitonclick()
