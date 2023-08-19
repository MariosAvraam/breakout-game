import turtle
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard

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
number_of_bricks_per_row = 10
number_of_rows = 4  # Adjust this to add more rows
brick_width = 60
total_bricks_width = number_of_bricks_per_row * brick_width
starting_x = -total_bricks_width / 2 + brick_width / 2  - 4
y_position = 170  # Adjusted from 200 to 180

for row in range(number_of_rows):
    x_position = starting_x
    for _ in range(number_of_bricks_per_row):
        brick = Brick(x_position, y_position)
        bricks.append(brick)
        x_position += brick_width
    y_position -= 30  # Move to the next row, 30 units below the previous one


# Create scoreboard
scoreboard = Scoreboard()


# Set up the keyboard bindings
screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")


game_state = ""
while game_state != "Game Over":
    screen.update()
    game_state = ball.move(paddle, bricks, scoreboard)
    turtle.time.sleep(0.017)  # 60 frames per second

# Display Game Over message
scoreboard.game_over()

# Keep the window open until it's clicked
screen.exitonclick()

