from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt") as f:
                self.high_score = int(f.read())
        except FileNotFoundError:
            self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        # Create a separate turtle for Game Over text so scoreboard stays at top
        game_over_turtle = Turtle()
        game_over_turtle.hideturtle()
        game_over_turtle.color("white")
        game_over_turtle.penup()
        game_over_turtle.goto(0, 0)
        game_over_turtle.write("GAME OVER\nPress 'R' to Restart", align=ALIGNMENT, font=FONT)
