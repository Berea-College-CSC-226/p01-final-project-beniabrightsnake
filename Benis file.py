import turtle
class GameScreen:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Bombastic Boa")
        self.screen.bgcolor("Black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)
game_screen = GameScreen()
game_screen.screen.exitonclick()