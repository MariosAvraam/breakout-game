import turtle

class Scoreboard:
    """
    Represents the scoreboard in the Breakout game.
    Manages and displays the score, game over message, and congratulatory message.
    """
    
    def __init__(self):
        """
        Initialize the scoreboard with default attributes and position it at the top center of the screen.
        """
        self.score = 0
        self.display = turtle.Turtle()
        self.display.speed(0)  # Maximum drawing speed
        self.display.color("white")
        self.display.penup()
        self.display.hideturtle()  # Hide the turtle icon
        self.display.goto(0, 180)  
        self.update_score()

    def update_score(self):
        """
        Clear the current score display and show the updated score.
        """
        self.display.clear()
        self.display.write("Score: {}".format(self.score), align="center", font=("Courier", 24, "normal"))

    def add_point(self):
        """
        Increment the score by one and update the display.
        """
        self.score += 1
        self.update_score()

    def game_over(self):
        """
        Display the 'Game Over' message at the center of the screen.
        """
        self.display.goto(0, 0)
        self.display.write("Game Over", align="center", font=("Courier", 36, "normal"))

    def congratulate(self):
        """
        Display the 'Well Done!' message at the center of the screen.
        """
        self.display.clear()
        self.display.goto(0, 0)
        self.display.write("Well Done!", align="center", font=("Courier", 36, "normal"))
