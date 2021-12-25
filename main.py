from turtle import Screen, Turtle
from typing import List, Text
from paddle import Paddle
from ball import Ball
from brick import Brick
from text import Text

import time


def build_wall():
    wall = []
    colours = ['blue', 'green', 'yellow', 'orange', 'red']
    for i in range(5):
        for j in range(10):
            position = (-590 + j * 130, 100 + 50 * i)
            brick = Brick(position, colours[i])
            wall.append(brick)

    return wall


def main():
    # Setup screen
    screen = Screen()
    screen.bgcolor("black")
    screen.title("Breakout")
    screen.tracer(0)
    screen.setup(height=800, width=1400)

    paddle = Paddle()
    ball = Ball()
    wall = build_wall()
    text = Text()

    screen.listen()
    screen.onkeypress(paddle.move_left, 'Left')
    screen.onkeypress(paddle.move_right, 'Right')

    game_is_on = True
    while game_is_on:
        time.sleep(0.01)
        ball.move()

        # Detect collision with side walls
        if ball.xcor() < -680 or ball.xcor() > 680:
            ball.flip_x()

        # Detect collision with ceiling
        if ball.ycor() > 390:
            ball.flip_y()

        # Detect collision with floor
        if ball.ycor() < -390:
            # game_is_on = False
            # text.game_over()
            ball.flip_y()

        if len(wall) == 0:
            text.winner()

        # Detect collision with paddle
        if abs(ball.xcor() - paddle.xcor()) < 70 and abs(ball.ycor() - paddle.ycor()) < 20:
            ball.flip_y()
            if (ball.xcor() - paddle.xcor() < 0 and ball.velocity_x > 0) or (ball.xcor() - paddle.xcor() > 0 and ball.velocity_x < 0):
                ball.flip_x()

            # Changing the angle of the ball
            ball.set_velocity_x(abs((ball.xcor() - paddle.xcor()) / 7))

        # Detect collision with bricks
        for brick in wall:
            destroyed = False
            if abs(ball.xcor() - brick.xcor()) < 70 and abs(ball.ycor() - brick.ycor()) < 10:
                ball.flip_x()
                destroyed = True
            elif abs(ball.xcor() - brick.xcor()) < 60 and abs(ball.ycor() - brick.ycor()) < 30:
                ball.flip_y()
                destroyed = True

            if destroyed:
                brick.hideturtle()
                wall.remove(brick)
                text.increase_score()
                # Increase speed of the ball depending on how many bricks are destroyed
                if len(wall) % 5 == 0:
                    ball.increase_speed()

        screen.update()
    screen.exitonclick()


# Executes the main function
if __name__ == '__main__':
    main()
