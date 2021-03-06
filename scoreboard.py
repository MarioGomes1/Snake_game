from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.clear()

    def score_tracker(self):
        self.write(arg=f"Score {self.score}", move=False, align='left', font=('Arial', 24, 'normal'))
        self.hideturtle()

    def refresh(self):
        self.score += 1
        self.write(arg=f"Score {self.score}", move=False, align='left', font=('Arial', 25, 'normal'))
        self.hideturtle()
        print(self.score)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align='left', font=('Arial', 25, 'normal'))