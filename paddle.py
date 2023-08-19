import turtle

class Paddle:
    """
    Represents the paddle in the Breakout game.
    Handles the paddle's movements and its visual representation.
    """
    
    def __init__(self):
        """
        Initialize the paddle with default attributes and position it at the bottom center of the screen.
        """
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)  # Maximum drawing speed
        self.paddle.shape("square")  # Base shape for the paddle
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)  # Adjust the paddle size
        self.paddle.penup()
        self.paddle.goto(0, -200)  # Starting position of the paddle
        
    def move_left(self, game_started):
        """
        Move the paddle to the left by a fixed amount.
        """
        if not game_started:
            return
        x = self.paddle.xcor()
        x -= 20  # Amount to move left
        self.paddle.setx(x)

    def move_right(self, game_started):
        """
        Move the paddle to the right by a fixed amount.
        """
        if not game_started:
            return
        x = self.paddle.xcor()
        x += 20  # Amount to move right
        self.paddle.setx(x)
