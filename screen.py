from turtle import Screen
class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.init_screen()
        self.screen.tracer(0)

    def init_screen(self):
        """
        initializes the screen
        """
        self.screen.bgcolor('black')
        self.screen.title("Pong Game")
        self.screen.setup(width=600, height=600)
