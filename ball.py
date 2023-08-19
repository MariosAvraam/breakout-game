import turtle

class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(20)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 3  # Delta/change in x - controls the ball's x direction
        self.ball.dy = 3  # Delta/change in y - controls the ball's y direction

    def move(self, paddle, bricks, scoreboard):
        # Move the ball based on its dx and dy
        x = self.ball.xcor() + self.ball.dx
        y = self.ball.ycor() + self.ball.dy
        
        # Boundary checking
        # Top Wall
        if y > 215:
            y = 215
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

         # Ball-Paddle Collision
        if (self.ball.dy < 0 and  # Ensure the ball is moving downward
            self.ball.ycor() - 10 <= paddle.paddle.ycor() + 10 and
            self.ball.xcor() > paddle.paddle.xcor() - 50 and
            self.ball.xcor() < paddle.paddle.xcor() + 50):
            
            self.ball.sety(paddle.paddle.ycor() + 20)  # Position the ball slightly above the paddle
            self.ball.dy *= -1  # Reverse the y direction

        # Ball-Brick Collision
        for brick in bricks:
            if (self.ball.distance(brick.brick) < 25):
                brick.brick.hideturtle()
                bricks.remove(brick)
                scoreboard.add_point()

                self.ball.dy *= -1        # Reverse the ball's y-direction
                break  # Exit the loop once a collision is detected

        # Check if ball misses the paddle and goes out of bounds
        if self.ball.ycor() < -240:
            return "Game Over"


    # ... (More methods related to ball collision will be added later)
