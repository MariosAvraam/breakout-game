import turtle

class Paddle:
    def __init__(self):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        self.paddle.goto(0, -200)
        
    def move_left(self):
        x = self.paddle.xcor()
        x -= 20
        self.paddle.setx(x)

    def move_right(self):
        x = self.paddle.xcor()
        x += 20
        self.paddle.setx(x)
