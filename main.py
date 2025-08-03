import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from sound import SoundEffects
import time

# SET UP THE MAIN SCREEN
screen = Screen()
screen.tracer(0)
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor("Black")

# CREATE 2 PADDLES
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = ScoreBoard()
sound = SoundEffects()

screen.listen()
#RIGHT PADDLE LISTENERS
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")

# LEFT PADDLE LISTENERS
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down,"s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


# AI paddle movement: only reacts if ball is nearby, on left side, and passes a 50% chance.
    if ball.xcor() < 0 and abs(ball.ycor() - l_paddle.ycor()) > 20:
        if random.random() > 0.5:
            if ball.ycor() > l_paddle.ycor():
                l_paddle.go_up()
            else:
                l_paddle.go_down()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 :
        ball.bounce_x()
        sound.play_collision()

    elif ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        sound.play_collision()

    if ball.xcor() > 370:
        ball.reset_game()
        scoreboard.l_point()

    if ball.xcor() < -370:
        sound.score_effect()
        ball.reset_game()
        scoreboard.r_point()

screen.exitonclick()