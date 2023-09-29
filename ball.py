from turtle import *


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.fillcolor('#445D48')
        self.setheading(270.0)
        self.speed_val = 3
        self.game_over = False


    def move(self):
        if -340 < self.position()[0] < 340 or -400 < self.position()[1] < 400:
            self.forward(self.speed_val)

    def check_player_collision(self, collide_object):
        if self.distance(collide_object) <= 20.0 or self.distance(x=collide_object.right[0], y=collide_object.right[1]) <= 25.0 or self.distance(x=collide_object.left[0], y=collide_object.left[1]) <= 25.0:
            self.change_direction(collide_object)
            return True
        return False

    def check_wall_collision(self):
        x = self.position()[0]
        y = self.position()[1]
        if x <= -390 or x >= 390 or y >= 290:
           return self.setheading(self.heading() + 90 % 360)
        if y <= -300:
            self.game_over = True
            self.speed_val = 0

    def check_bricks_collision(self, bricks):
        collided_min = 600
        pretendent = None

        for brick in bricks:
            if self.distance(brick) <= 20:
                pretendent_d = self.distance(brick)
                pretendent = brick if pretendent_d < collided_min else pretendent
                collided_min = min(pretendent_d, collided_min)

        if pretendent != None:
            self.setheading(self.heading() + 90 % 360)
            pretendent.hideturtle()
            return pretendent

    def change_direction(self, collide_object):
        new_direction = self.towards(collide_object) + 180 % 360
        self.setheading(new_direction)

