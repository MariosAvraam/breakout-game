import turtle
from paddle import Paddle
from ball import Ball
from brick import Brick

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=600, height=450)
screen.tracer(0)

# Create the paddle
paddle = Paddle()

# Create the ball
ball = Ball()

# Create bricks
bricks = []
number_of_bricks = 10
brick_width = 60  # Width of a brick including space between bricks
total_bricks_width = number_of_bricks * brick_width # 600
starting_x = -total_bricks_width / 2 + brick_width / 2  - 4 # Centering the bricks 
y_position = 200  # Adjusted y position

for _ in range(number_of_bricks):
    brick = Brick(starting_x, y_position)
    bricks.append(brick)
    starting_x += brick_width  # Space between bricks


# Set up the keyboard bindings
screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

# Main game loop
while True:
    ball.move(paddle)
    screen.update()
    turtle.time.sleep(0.017)  # 60 frames per second

