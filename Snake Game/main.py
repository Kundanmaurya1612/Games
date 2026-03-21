from snakeScreen import SnakeScreen
from snake import Snake
from turtle import Screen
from food import Food
from score import Score
screen = Screen()
snakeScreen = SnakeScreen()
snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.left,"a")
screen.onkey(snake.up,"w")
screen.onkey(snake.right,"d")
screen.onkey(snake.down,"s")

game_is_on = True
while game_is_on:
    snakeScreen.update()
    snake.move()

    #detect collison with food
    if snake.tims[0].distance(food) < 15:
        food.refresh()
        score.current_score +=1
        score.update()
        snake.extend()
        
    
    #detect collision with wall
    if snake.tims[0].xcor() > 280 or snake.tims[0].xcor() < -280 or snake.tims[0].ycor() > 280 or snake.tims[0].ycor() < -280:
        score.refresh()
        snake.refresh()
       
    #self collision detection
    for bite in snake.tims[1:]:
        if snake.tims[0].distance(bite) < 10:
           score.refresh()
           snake.refresh()

screen.exitonclick()


        
        
    
        
