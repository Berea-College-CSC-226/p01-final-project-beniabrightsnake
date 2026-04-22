import turtle
class GameScreen:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Benis Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

    def update(self):
        self.screen.update()

    def mainloop(self):
        self.screen.mainloop()

