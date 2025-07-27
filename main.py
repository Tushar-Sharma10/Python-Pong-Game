from turtle import Screen
from paddle import Paddle

# SET UP THE MAIN SCREEN
screen = Screen()
screen.tracer(0)
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor("Black")

# CREATE 2 PADDLES
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
#RIGHT PADDLE LISTENERS
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")

# LEFT PADDLE LISTENERS
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s")

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()