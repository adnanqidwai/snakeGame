from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 268)
        self.color("white")
        self.write(f"Score= {self.score} ", move=False, align="center", font=("Arial", 24, "normal"))

    def increasescore(self):
        self.score += 1
        self.clear()
        self.write(f"Score= {self.score} ", move=False, align="center", font=("Arial", 24, "normal"))
    def gameover(self):
        self.goto(0,0)
        self.color("white")
        self.write("GAME OVER \n click the screen to exit")