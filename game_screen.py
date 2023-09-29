from turtle import Screen
from game import Game

class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.title("Breakout")
        self.screen.bgcolor('#2E4374')
        self.screen.tracer(5)
        self.game = Game()
        self.screen.listen()
        self.paused = False
        self.screen.onkeypress(self.game.player.move_left, "Left")
        self.screen.onkeypress(self.game.player.move_right, "Right")
        self.screen.onkeypress(self.reset, "space")
        self.screen.onkeypress(self.pause, 'Escape')
    def reset(self):
        self.screen.clearscreen()
        self.__init__()

    def update(self):
        self.screen.update()
        if not self.paused:
            self.game.update()

    def pause(self):
        self.paused = not self.paused