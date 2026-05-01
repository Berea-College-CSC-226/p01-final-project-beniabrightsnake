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
            grid_painter.goto(x, 300);
            grid_painter.pendown();
            grid_painter.goto(x, -300)
        for y in range(-300, 301, 20):
            grid_painter.penup()
            grid_painter.goto(-400, y);
            grid_painter.pendown();
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
            e.shape("circle");
            e.shapesize(0.3, 0.3);
            e.color("black");
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
                self.eye_l.goto(hx - 6, hy + 6);
                self.eye_r.goto(hx + 6, hy + 6)
            elif self.direction == "down":
                self.eye_l.goto(hx - 6, hy - 6);
                self.eye_r.goto(hx + 6, hy - 6)
            elif self.direction == "left":
                self.eye_l.goto(hx - 6, hy + 6);
                self.eye_r.goto(hx - 6, hy - 6)
            elif self.direction == "right":
                self.eye_l.goto(hx + 6, hy + 6);
                self.eye_r.goto(hx + 6, hy - 6) #####


#     def add_segment(self, position, is_head=False):
# # class Snake:
# #     def __init__(self):
# #         self.segments = []
# #         self.create_snake()
# #         self.direction = "stop"
# #
# #     def create_snake(self):
# #         positions = [(0, 0), (-20, 0), (-40, 0)]
# #         for pos in positions:
# #             self.add_segment(pos)
# #
#     def add_segment(self, position):
#         segment = turtle.Turtle()
#         segment.shape("square")
#         segment.color("green")
#         segment.penup()
#         segment.goto(position)
#         self.segments.append(segment)
#
#     def move(self):
#         # move body (back to front)
#         for i in range(len(self.segments) - 1, 0, -1):
#             x = self.segments[i - 1].xcor()
#             y = self.segments[i - 1].ycor()
#             self.segments[i].goto(x, y)
#
#         # move head
#         head = self.segments[0]
#         if self.direction == "up":
#             head.sety(head.ycor() + 20)
#         elif self.direction == "down":
#             head.sety(head.ycor() - 20)
#         elif self.direction == "left":
#             head.setx(head.xcor() - 20)
#         elif self.direction == "right":
#             head.setx(head.xcor() + 20)
#
#     def go_up(self):
#         if self.direction != "down":
#             self.direction = "up"
#
#     def go_down(self):
#         if self.direction != "up":
#             self.direction = "down"
#
#     def go_left(self):
#         if self.direction != "right":
#             self.direction = "left"
#
#     def go_right(self):
#         if self.direction != "left":
#             self.direction = "right"
# game_screen = GameScreen()
# snake = Snake()
#
# screen = game_screen.screen
#
# # controls
# screen.listen()
# screen.onkey(snake.go_up, "Up")
# screen.onkey(snake.go_down, "Down")
# screen.onkey(snake.go_left, "Left")
# screen.onkey(snake.go_right, "Right")
# running = True
# while True:
#     screen.update()
#     snake.move()
#     time.sleep(0.1)
#
# screen.exitonclick()