from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.title("PongGame")
screen.setup(width=900, height=600)
screen.tracer(0)

ball = Ball()

l_paddle = Paddle((-400,0))
r_paddle = Paddle((400,0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    #move ball
    ball.move()

    #detect colision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    #detect colision with paddle
    if ball.distance(r_paddle) < 55 and ball.xcor() >380 or ball.distance(l_paddle) < 55 and ball.xcor() <-380:
        ball.bounce_paddle()

    #detect right paddles misses
    if ball.xcor() > 450:
        ball.reset()
        scoreboard.l_point()
    
    #detect left paddles misses
    if ball.xcor() < -450:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()