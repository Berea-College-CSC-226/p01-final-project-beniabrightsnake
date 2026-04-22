#from Benis_file import *
# Segment-based Snake
import turtle
import time
class GameScreen:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Bombastic Boa")
        self.screen.bgcolor("Black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.direction = "stop"

    def create_snake(self):
        positions = [(0, 0), (-20, 0), (-40, 0)]
        for pos in positions:
            self.add_segment(pos)

    def add_segment(self, position):
        segment = turtle.Turtle()
        segment.shape("square")
        segment.color("green")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        # move body (back to front)
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

        # move head
        head = self.segments[0]
        if self.direction == "up":
            head.sety(head.ycor() + 20)
        elif self.direction == "down":
            head.sety(head.ycor() - 20)
        elif self.direction == "left":
            head.setx(head.xcor() - 20)
        elif self.direction == "right":
            head.setx(head.xcor() + 20)

    def go_up(self):
        if self.direction != "down":
            self.direction = "up"

    def go_down(self):
        if self.direction != "up":
            self.direction = "down"

    def go_left(self):
        if self.direction != "right":
            self.direction = "left"

    def go_right(self):
        if self.direction != "left":
            self.direction = "right"
game_screen = GameScreen()
snake = Snake()

screen = game_screen.screen

# controls
screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")
running = True
while True:
    screen.update()
    snake.move()
    time.sleep(0.1)

screen.exitonclick()