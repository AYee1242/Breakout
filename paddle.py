from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.penup()
        self.goto((0, -360))

    def move_right(self):
        self.setx(self.xcor() + 20)

    def move_left(self):
        self.setx(self.xcor() - 20)
