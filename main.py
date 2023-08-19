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
number_of_rows = 3  # Adjust this to add more rows
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

start_message = turtle.Turtle()
start_message.speed(0)
start_message.color("white")
start_message.penup()
start_message.hideturtle()
start_message.goto(0, 0)
start_message.write("Press 'S' to Start", align="center", font=("Courier", 36, "normal"))
def start_game():
    global game_started
    start_message.clear()
    game_started = True

game_started = False

# Set up the keyboard bindings
screen.listen()
screen.onkeypress(lambda: paddle.move_left(game_started), "Left")
screen.onkeypress(lambda: paddle.move_right(game_started), "Right")
screen.onkeypress(start_game, "s")

# Wait for the game to start
while not game_started:
    screen.update()

# Main game loop
game_state = ""
while game_state != "Game Over":
    screen.update()
    game_state = ball.move(paddle, bricks, scoreboard)
    if not bricks:
        scoreboard.congratulate()
        screen.update()
        screen.exitonclick()  # Wait for user click before closing the window
    turtle.time.sleep(0.017)  # 60 frames per second

# Display Game Over message
scoreboard.game_over()

# Keep the window open until it's clicked
screen.exitonclick()