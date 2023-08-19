import turtle
from random import choice

class Brick:
    """
    Represents a brick in the Breakout game.
    Each brick has a random color from a predefined list.
    """
    
    COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "cyan", "white", 
              "pink", "lime", "magenta", "navy", "turquoise", "gold", "coral", 
              "chocolate", "salmon", "ivory", "maroon", "olive"]
    
    def __init__(self, x, y):
        """
        Initialize a brick with a random color and position it at the specified (x, y) coordinates.

        Args:
            x (int): The x-coordinate for the brick's position.
            y (int): The y-coordinate for the brick's position.
        """
        
        self.brick = turtle.Turtle()
        self.brick.speed(0)  # Maximum drawing speed
        self.brick.shape("square")
        self.brick.color(choice(self.COLORS))  # Randomly choose a color for the brick
        self.brick.shapesize(stretch_wid=1, stretch_len=2)  # Adjust the brick size
        self.brick.penup()
        self.brick.goto(x, y)
