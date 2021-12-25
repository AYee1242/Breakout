from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -200)
        self.velocity_x = random.randint(-5, 5) + 1
        self.velocity_y = 10

    def move(self):
        new_y = self.ycor() + self.velocity_y
        new_x = self.xcor() + self.velocity_x
        self.goto(new_x, new_y)

    def flip_x(self):
        self.velocity_x *= -1

    def flip_y(self):
        self.velocity_y *= -1

    def set_velocity_x(self, magnitude):
        direction = self.velocity_x / abs(self.velocity_x)
        print(magnitude)
        print(direction)
        self.velocity_x = magnitude * direction
        print(self.velocity_x)

    def increase_speed(self):
        self.velocity_y *= 1.1
