from turtle import Turtle


class Brick(Turtle):

    def __init__(self, position, colour) -> None:
        super().__init__()
        self.shape('square')
        self.color('black', colour)
        self.shapesize(stretch_wid=2, stretch_len=6, outline=5)
        self.penup()
        self.goto(position)
