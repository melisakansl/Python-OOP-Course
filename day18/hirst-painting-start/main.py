###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import turtle as turtle_module
import random
# import colorgram
me = turtle_module.Turtle()
turtle_module.colormode(255)


# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

my_colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123),
             (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
             (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
             (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
             (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# my_t.dot(20,random.choice(my_colors))
me.penup()
me.right(180)
me.forward(250)
me.right(90)
me.forward(250)
me.right(90)
me.speed("fastest")

for column in range(10):
    for row in range(10):
        color_rgb = random.choice(my_colors)
        me.fillcolor(color_rgb)
        me.pencolor(color_rgb)
        me.begin_fill()
        me.circle(10)
        me.end_fill()
        me.penup()
        me.forward(50)
        me.pendown()
    me.penup()
    me.left(90)
    me.forward(10)
    me.left(90)
    me.forward(500)
    me.left(90)
    me.forward(50)
    me.left(90)
    me.pendown()
screen = turtle_module.Screen()
screen.exitonclick()