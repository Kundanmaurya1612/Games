from turtle import Turtle, Screen
from tim import Tim,Bots,Lines,Score,GameOver
import random

screen = Screen()
screen.setup(800,600)
screen.bgcolor("#232323")
screen.tracer(0)

lines1 = Lines((400,-240))
lines2 = Lines((400,240))
lines1.pendown()
lines2.pendown()
for i in range(80):
    lines1.forward(10)
    lines1.penup()
    lines1.forward(10)
    lines1.pendown()
    lines2.forward(10)
    lines2.penup()
    lines2.forward(10)
    lines2.pendown()


tim = Tim()
game = GameOver()
score = Score()
screen.listen()
screen.onkeypress(tim.move,"w")

botlist = []

screen.tracer(1)

# i = 0
game_is_on = True
# while game_is_on:
#     i += 1
#     time.sleep(.1)
#     screen.tracer(0)

#     #tim at finish line
#     if tim.ycor() == 250:
#         score.increase()
#         tim.goto(-70,-270)

#     #bot spawn logic    
#     if 
#     # if i == 200:
#     #     game_is_on = False
#     for car in botlist:
#         car.forward(3)
#     for car in botlist:
#         if car.xcor() <= -410:
#             car.hideturtle()
#             botlist.remove(car)
#     screen.tracer(1)
def game_loop():
    global game_is_on
    if not game_is_on:
        return
    # Spawn new bot occasionally
    if score.current_score < 4:
        if random.randint(1, score.current_score+1) == 1:
            botlist.append(Bots())
    else:
        if random.randint(1, score.current_score) == 1:
            botlist.append(Bots())
    #tim at finish line
    if tim.ycor() > 250:
        score.increase()
        tim.goto(-70,-270)

    # Move all enemies
    for bot in botlist:
        bot.setx(bot.xcor()-10-(score.current_score*1.5))
    
    #collison detect
    for bot in botlist:
        if tim.distance(bot) < 15:
            game.over()
            game_is_on = False

    #remove garbage turtle from list
    for car in botlist:
        if car.xcor() <= -410:
            car.hideturtle()
            botlist.remove(car)
        
    screen.update()
    screen.ontimer(game_loop, 100)

screen.tracer(0)
game_loop()
    

screen.exitonclick()