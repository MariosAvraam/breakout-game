import turtle
from random import choice

class Brick:
    COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "cyan", "white", "pink", "lime", "magenta", "navy", "turquoise", "gold", "coral", "chocolate", "salmon", "ivory", "maroon", "olive"]
    def __init__(self, x, y):
        self.brick = turtle.Turtle()
        self.brick.speed(0)
        self.brick.shape("square")
        self.brick.color(choice(self.COLORS))
        self.brick.shapesize(stretch_wid=1, stretch_len=2)  # Adjust the brick size
        self.brick.penup()
        self.brick.goto(x, y)
