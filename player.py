from turtle import *


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.fillcolor('#FDE5D4')
        self.shapesize(stretch_len=5)
        self.penup()
        self.speed(0)
        self.sety(-200)
        self.speed(1)
        self.update_position()

    def move_left(self):
        if self.position()[0] > -340:
            self.backward(15)
            self.update_position()

    def move_right(self):

        if self.position()[0] < 340:
            self.forward(15)
            self.update_position()

    def update_position(self):
        self.left = (self.position()[0] - 25, self.position()[1])
        self.right = (self.position()[0] + 25, self.position()[1])

