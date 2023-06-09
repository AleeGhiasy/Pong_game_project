from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 230)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def add_score_left(self):
        self.clear()
        self.l_score +=1
        self.update_scoreboard()

    def add_score_right(self):
        self.clear()
        self.r_score +=1
        self.update_scoreboard()
