from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.highscore = self.read_high_score()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-100, y=240)
        self.write(f"AI = {self.l_score} USER = {self.r_score} Highest= {self.highscore}", align="center",
                   font=("Courier", 35, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        if self.r_score > self.highscore:
            self.highscore = self.r_score
            self.write_high_score()
        self.update_score()

    def read_high_score(self):
        try:
            with open("highscore.txt", mode="r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0

    def write_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.highscore))
