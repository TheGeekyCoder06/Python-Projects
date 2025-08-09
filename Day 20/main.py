import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

# Create objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Game state flags
game_is_on = True
game_paused = False  # Becomes True after Game Over

# Movement controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Restart function
def restart_game():
    global game_paused
    if game_paused:
        scoreboard.save_high_score()
        scoreboard.reset_score()
        snake.reset()
        food.refresh()
        game_paused = False

# Bind restart key
screen.onkey(restart_game, "r")

# Game loop
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if not game_paused:
        snake.move()

        # Collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Collision with wall
        if (
            snake.head.xcor() > 280 or
            snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or
            snake.head.ycor() < -280
        ):
            scoreboard.game_over()
            game_paused = True

        # Collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_paused = True

screen.exitonclick()
