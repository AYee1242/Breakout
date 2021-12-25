from turtle import Turtle
ALIGNMENT = "center"


class Text(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 330)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        font = ("Courier", 30, "normal")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=font)

    def game_over(self):
        font = ("Courier", 50, "normal")
        self.goto(0, -200)
        self.write("GAME OVER", align=ALIGNMENT, font=font)

    def winner(self):
        font = ("Courier", 50, "normal")
        self.goto(0, 0)
        self.write("WINNER", align=ALIGNMENT, font=font)

    def increase_score(self):
        self.score += 100
        self.clear()
        self.update_scoreboard()
