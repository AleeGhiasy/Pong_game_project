from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Score
import time
screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

#creating the paddle
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
score = Score()
screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

game_on = True
while game_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move_ball()

    #check for wall
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.y_bounce()
    #check for paddles if the ball touches one of them
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor() < -320:
        ball.x_bounce()
        ball.speed
    #check if the ball touched the right wall
    if ball.xcor()> 380:
        ball.reset_position()
        score.add_score_left()
    #check if the ball touched the left wall
    if ball.xcor()< -380:
        ball.reset_position()
        score.add_score_right()

screen.exitonclick()