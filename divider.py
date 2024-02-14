from turtle import Turtle


class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pensize(15)
        self.color("white")
        self.hideturtle()
        self.goto(-325, 0)
        self.draw_divider()

    def draw_divider(self):
        for i in range(12):
            if i % 2 != 0:
                self.pendown()
            else:
                self.penup()
            self.forward(50)