import turtle

class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(20)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 1  # Delta/change in x - controls the ball's x direction
        self.ball.dy = 1  # Delta/change in y - controls the ball's y direction

    def move(self):
        # Move the ball based on its dx and dy
        x = self.ball.xcor() + self.ball.dx
        y = self.ball.ycor() + self.ball.dy
        
        # Boundary checking
        # Top Wall
        if y > 215:
            y = 215
            self.ball.dy *= -1  # Reverse the y direction

        # Bottom Wall
        if y < -210:
            y = -210
            self.ball.dy *= -1  # Reverse the y direction

        # Right Wall
        if x > 285:
            x = 285
            self.ball.dx *= -1  # Reverse the x direction

        # Left Wall
        if x < -290:
            x = -290
            self.ball.dx *= -1  # Reverse the x direction
        
        self.ball.setx(x)
        self.ball.sety(y)
    # ... (More methods related to ball collision will be added later)
