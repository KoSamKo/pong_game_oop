from turtle import Turtle
import random

COLORS = ["white", "yellow", "silver", "green", "orange"]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_move = 9
        self.y_move = 9
        self.move_speed = 0.08
        

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def reset(self):
        self.color(random.choice(COLORS))
        self.goto(0,0)
        self.increase_speed()

    def increase_speed(self):
        self.move_speed *= 0.9