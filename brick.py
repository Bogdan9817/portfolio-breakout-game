from turtle import *

class Brick(Turtle):

    def __init__(self, color, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1.5)
        self.fillcolor(color)
        self.speed(0)
        self.penup()
        self.setpos(x=pos[0], y=pos[1])
        self.left = (self.position()[0] - 20, self.position()[1])
        self.right = (self.position()[0] + 20, self.position()[1])