from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.penup()
        self.shapesize(stretch_wid= 5, stretch_len = 1)
        self.goto(position)

    def go_up(self):
        """ Will move the paddle upwards by 20"""
        y_cor = self.ycor()
        self.sety(y_cor + 20)

    def go_down(self):
        """ Will move the paddle downwards by 20"""
        y_cor = self.ycor()
        self.sety(y_cor - 20)



