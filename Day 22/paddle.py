from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < 250:  # top limit
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -250:  # bottom limit
            self.goto(self.xcor(), self.ycor() - 20)
