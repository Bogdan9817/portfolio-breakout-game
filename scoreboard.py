from turtle import *

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.sety(-270)
        self.setx(-50)
        self.fillcolor('#FDE5D4')
        self.color("#FDE5D4")
        self.write("Your score: ", font=('Verdana', 24, "normal"))

    def update_score(self, score):
        self.clear()
        self.write(f"Your score: {score}", font=('Verdana', 24, "normal"))

    def write_over(self):
        self.sety(0)
        self.write("Game over!", font=('Verdana', 24, "normal"))