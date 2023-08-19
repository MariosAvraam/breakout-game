import turtle

class Ball:
    """
    Represents the ball in the Breakout game.
    Handles the ball's movements, collisions with the paddle, bricks, and boundaries.
    """

    def __init__(self):
        """
        Initialize the ball with default attributes.
        """
        self.ball = turtle.Turtle()
        self.ball.speed(20)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 3  # Delta/change in x - controls the ball's x direction
        self.ball.dy = 3  # Delta/change in y - controls the ball's y direction

    def move(self, paddle, bricks, scoreboard):
        """
        Move the ball and handle its interactions with the paddle, bricks, and boundaries.
        
        Args:
            paddle (Paddle): The game's paddle object.
            bricks (list): A list containing the game's Brick objects.
            scoreboard (Scoreboard): The game's scoreboard object.
            
        Returns:
            str: "Game Over" if the ball goes out of bounds at the bottom, None otherwise.
        """
        
        # Update the ball's position based on its dx and dy
        x = self.ball.xcor() + self.ball.dx
        y = self.ball.ycor() + self.ball.dy
        
        # Boundary checking
        if y > 215 or y < -240:
            self.ball.dy *= -1  # Reverse the y direction
        
        if x > 285 or x < -290:
            self.ball.dx *= -1  # Reverse the x direction
        
        self.ball.setx(x)
        self.ball.sety(y)

        # Ball-Paddle Collision
        if (self.ball.dy < 0 and  # Ensure the ball is moving downward
            self.ball.ycor() - 10 <= paddle.paddle.ycor() + 10 and
            paddle.paddle.xcor() - 50 < self.ball.xcor() < paddle.paddle.xcor() + 50):
            
            self.ball.sety(paddle.paddle.ycor() + 20)  # Position the ball slightly above the paddle
            self.ball.dy *= -1  # Reverse the y direction

        # Ball-Brick Collision
        for brick in bricks:
            if self.ball.distance(brick.brick) < 25:
                brick.brick.hideturtle()
                bricks.remove(brick)
                scoreboard.add_point()
                self.ball.dy *= -1  # Reverse the ball's y-direction
                break  

        # Check if ball misses the paddle and goes out of bounds
        if self.ball.ycor() < -240:
            return "Game Over"
