# from Benis_file import *
# Segment-based Snake
import turtle
import time
import random


class GameScreen:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Bombastic Boa: Rain Escape")
        self.screen.bgcolor("#0a0a0a")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)
        self.draw_grid()
    def draw_grid(self):
        grid_painter = turtle.Turtle()
        grid_painter.hideturtle()
        grid_painter.speed(0)
        grid_painter.color("#001a00")
        for x in range(-400, 401, 20):
            grid_painter.penup()
            grid_painter.goto(x, 300)
            grid_painter.pendown()
            grid_painter.goto(x, -300)
        for y in range(-300, 301, 20):
            grid_painter.penup()
            grid_painter.goto(-400, y)
            grid_painter.pendown()
            grid_painter.goto(400, y)

class Snake:
    def __init__(self):
        self.segments = []
        self.direction = "stop"
        self.create_snake()
        self.eye_l = turtle.Turtle()
        self.eye_r = turtle.Turtle()
        for e in [self.eye_l, self.eye_r]:
            e.penup();
            e.shape("circle")
            e.shapesize(0.3, 0.3)
            e.color("black")
            e.speed(0)
    def create_snake(self):
        positions = [(0, -200), (-20, -200), (-40, -200)]
        for i, pos in enumerate(positions):
            self.add_segment(pos, is_head=(i == 0))

    def add_segment(self, position, is_head=False):
        segment = turtle.Turtle()
        segment.shape("square")
        segment.color("#2ecc71") if is_head else segment.color("#27ae60")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        if self.direction == "stop": return
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
        head = self.segments[0]
        if self.direction == "up":
            head.sety(head.ycor() + 20)
        elif self.direction == "down":
            head.sety(head.ycor() - 20)
        elif self.direction == "left":
            head.setx(head.xcor() - 20)
        elif self.direction == "right":
            head.setx(head.xcor() + 20)


    def update_eyes(self):
        head = self.segments[0]
        hx, hy = head.xcor(), head.ycor()
        if self.direction == "up" or self.direction == "stop":
             self.eye_l.goto(hx - 6, hy + 6)
             self.eye_r.goto(hx + 6, hy + 6)
        elif self.direction == "down":
             self.eye_l.goto(hx - 6, hy - 6)
             self.eye_r.goto(hx + 6, hy - 6)
        elif self.direction == "left":
             self.eye_l.goto(hx - 6, hy + 6)
             self.eye_r.goto(hx - 6, hy - 6)
        elif self.direction == "right":
             self.eye_l.goto(hx + 6, hy + 6)
             self.eye_r.goto(hx + 6, hy - 6)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def go_up(self):
        if self.direction != "down": self.direction = "up"

    def go_down(self):
        if self.direction != "up": self.direction = "down"

    def go_left(self):
        if self.direction != "right": self.direction = "left"

    def go_right(self):
        if self.direction != "left": self.direction = "right"

class Faller(turtle.Turtle):
        def __init__(self, item_type):
            super().__init__()
            self.item_type = item_type
            self.penup()
            if self.item_type == "fruit":
                self.shape("circle")
                self.color("#ff4757")
                self.shapesize(0.9, 0.9)
            else:
                self.shape("square")
                self.color("#57606f")
                self.shapesize(1.4, 1.4)
            self.respawn(initial_spawn=True)

        def respawn(self, initial_spawn=False):
            x = random.randint(-19, 19) * 20
            y = random.randint(300, 600) if initial_spawn else random.randint(320, 500)
            self.goto(x, y)

        def fall(self, speed):
            self.sety(self.ycor() - speed)


def main():
    game_screen = GameScreen()
    snake = Snake()
    screen = game_screen.screen

    hud = turtle.Turtle()
    hud.hideturtle()
    hud.color("white")
    hud.penup()
    hud.goto(-380, 260)

    legend = turtle.Turtle()
    legend.hideturtle()
    legend.penup()
    legend.color("#ff4757")
    legend.goto(60, 270)
    legend.write("● FRUIT (CATCH)", font=("Courier", 10, "bold"))
    legend.color("#7f8c8d")
    legend.goto(185, 270)
    legend.write("| ■ BOMB (DODGE)", font=("Courier", 10, "bold"))

    screen.listen()
    screen.onkey(snake.go_up, "Up")
    screen.onkey(snake.go_down, "Down")
    screen.onkey(snake.go_left, "Left")
    screen.onkey(snake.go_right, "Right")

    score, wave = 0, 1
    fall_speed = 6.0
    game_speed = 0.15

    fallers = [Faller("fruit")]
    for _ in range(3):
        fallers.append(Faller("bomb"))

    running = True
    while running:
        hud.clear()
        hud.write(f"Score: {score}  Wave: {wave}", font=("Courier", 16, "bold"))

        screen.update()
        snake.move()
        snake.update_eyes()

        head = snake.segments[0]

        if abs(head.xcor()) > 390 or abs(head.ycor()) > 290:
            running = False

        for f in fallers:
            f.fall(fall_speed)

            if f.distance(head) < 25:
                if f.item_type == "bomb":
                    running = False
                else:
                    score += 10
                    snake.grow()
                    f.respawn()
                    wave += 1
                    fall_speed += 0.5
                    game_speed *= 0.96
                    if game_speed < 0.04:
                        game_speed = 0.04
                    if wave % 3 == 0:
                        fallers.append(Faller("bomb"))

            if f.ycor() < -310:
                if f.item_type == "fruit":
                    running = False
                else:
                    f.respawn()

        time.sleep(game_speed)

    hud.goto(0, 0)
    hud.color("#e74c3c")
    hud.write("GAME OVER", align="center", font=("Courier", 40, "bold"))
    hud.goto(0, -40)
    hud.color("white")
    hud.write(f"Final Score: {score}", align="center", font=("Courier", 18, "normal"))

    screen.update()
    screen.exitonclick()

if __name__ == "__main__":
    main()

