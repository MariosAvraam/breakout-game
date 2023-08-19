import turtle

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.display = turtle.Turtle()
        self.display.speed(0)
        self.display.color("white")
        self.display.penup()
        self.display.hideturtle()
        self.display.goto(0, 180)  # Adjusted from 210 to 180
        self.update_score()

    def update_score(self):
        self.display.clear()
        self.display.write("Score: {}".format(self.score), align="center", font=("Courier", 24, "normal"))

    def add_point(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.display.goto(0, 0)
        self.display.write("Game Over", align="center", font=("Courier", 36, "normal"))
