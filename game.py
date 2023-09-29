from player import Player
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard

class Game:

    def __init__(self):
        self.player = Player()
        self.ball = Ball()
        self.scoreboard = Scoreboard()
        self.bricks = []
        self.score = 0
        self.render_bricks()

    def render_bricks(self):
        for y in range(270, 180, -30):
            for x in range(-400, 400, 40):
                brick = Brick(color="Yellow", pos=(x, y))
                self.bricks.append(brick)

    def update(self):
        self.ball.move()
        self.ball.check_player_collision(self.player)
        self.ball.check_wall_collision()

        brick_to_delete = self.ball.check_bricks_collision(self.bricks)
        if brick_to_delete in self.bricks:
            self.bricks.remove(brick_to_delete)
            self.score += 1
            self.scoreboard.update_score(self.score)
        if self.ball.game_over:
            self.scoreboard.write_over()
