from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.left(180)
    tim.forward(10)
    tim.right(180)


def move_up():
    tim.left(90)
    tim.forward(10)
    tim.right(90)


def move_down():
    tim.right(90)
    tim.forward(10)
    tim.left(90)


def clear():
    tim.clear()
    tim.home()


screen.listen()

screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="d", fun=move_forwards)
screen.onkey(key="a", fun=move_backwards)
screen.onkey(key="c", fun= clear)
screen.exitonclick()
