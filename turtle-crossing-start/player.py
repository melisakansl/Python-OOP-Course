from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.hideturtle()
        self.go_to_starting_point()
        self.setheading(90)
        self.showturtle()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_to_starting_point(self):
        self.penup()
        self.goto(STARTING_POSITION)

    def successful_cross(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
