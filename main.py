import turtle
from paddle import Paddle

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=600, height=450)
screen.tracer(0)

# Create the paddle
paddle = Paddle()

# Set up the keyboard bindings
screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

# Main game loop
while True:
    screen.update()
    turtle.time.sleep(0.017)  # 60 frames per second