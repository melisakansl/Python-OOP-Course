from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-270,260)
        self.color("navy")
        self.hideturtle()
        self.write("Score: 0 ", align="left", font=FONT)
        self.score = 0

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=FONT)
