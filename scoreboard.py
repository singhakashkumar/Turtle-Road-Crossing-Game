from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 260)
        self.level = 1
        self.output()

    def output(self):
        self.clear()
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def level_up(self):
        self.level += 1
        self.output()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER :(", align="Center", font=FONT)


