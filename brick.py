import turtle

class Brick:
    def __init__(self, x, y):
        self.brick = turtle.Turtle()
        self.brick.speed(0)
        self.brick.shape("square")
        self.brick.color("white")
        self.brick.shapesize(stretch_wid=1, stretch_len=2)  # Adjust the brick size
        self.brick.penup()
        self.brick.goto(x, y)
