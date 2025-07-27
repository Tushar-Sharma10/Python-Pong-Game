from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
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


screen.listen()
#RIGHT PADDLE LISTENERS
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")

# LEFT PADDLE LISTENERS
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 :
        ball.bounce_x()

    elif ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 370:
        ball.reset_game()
        scoreboard.l_point()

    if ball.xcor() < -370:
        ball.reset_game()
        scoreboard.r_point()

screen.exitonclick()