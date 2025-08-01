from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 15
        self.x_move = 11
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)   # 11,255

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_game(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.bounce_x()

    def increase_speed(self):
        self.y_move += 1
        self.y_move += 1




