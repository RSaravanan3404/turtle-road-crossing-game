from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-280, 250)
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def update_level(self):
        self.level += 1
        self.show_level()

    def game_over(self):
        self.goto(0, 20)
        self.write("GAME OVER!", align="center", font=FONT)
