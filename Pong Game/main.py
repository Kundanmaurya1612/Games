from turtle import Screen
from paddel import Paddel
from ball import Ball
from random import randint


screen = Screen()
screen.bgcolor("#181818")
screen.title("Pong 1972")
screen.setup(900, 600)
ball = Ball()
ball.goto(0, 0)

screen.tracer(0)

paddel = Paddel((-440,0))
paddel2 = Paddel((430,0))


# Key Bindings
screen.onkeypress(paddel.t1_up_move_on, "w")
screen.onkeyrelease(paddel.t1_up_move_off, "w")
screen.onkeypress(paddel2.t2_up_move_on, "Up")
screen.onkeyrelease(paddel2.t2_up_move_off, "Up")
screen.onkeypress(paddel.t1_down_move_on, "s")
screen.onkeyrelease(paddel.t1_down_move_off, "s")
screen.onkeypress(paddel2.t2_down_move_on, "Down")
screen.onkeyrelease(paddel2.t2_down_move_off, "Down")
screen.listen()

def game_loop():
    if paddel.t1_up:
        paddel.sety(paddel.ycor() + 10)
    if paddel2.t2_up:
        paddel2.sety(paddel2.ycor() + 10)
    if paddel.t1_down:
        paddel.sety(paddel.ycor() - 10)
    if paddel2.t2_down:
        paddel2.sety(paddel2.ycor() - 10)

    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(paddel2) < 50 and ball.xcor() > 410) or (ball.distance(paddel) < 50 and ball.xcor() < -420):
        ball.bounce_x()

    
    screen.update() # Update both at once
    screen.ontimer(game_loop, 20) # Run at 50 FPS

game_loop()
screen.mainloop()