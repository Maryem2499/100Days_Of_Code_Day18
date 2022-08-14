# import turtle as t
# timmy = t.Turtle()
# Import our turtle module
from turtle import *
import heroes
print(heroes.gen())
timmy = Turtle()
timmy.color("black")
timmy.shape("turtle")

# TODO 1: Draw a square with turtle :
    # for _ in range(4):
    #     timmy.forward(100)
    #     timmy.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# TODO 2: Draw a DashedLine --------->
    # for a in range(15):
    #     timmy.forward(10)
    #     timmy.penup()
    #     timmy.forward(10)
    #     timmy.pendown()


# TODO 3:  Drawing Different Shapes with random/different colors
    # import random
    # colors = ["brown", "peru", "tan", "tomato", "light salmon", "peach puff", "dark salmon"]
    # def draw_shape(num_sides):
    #     angle = 360 / num_sides
    #     for i in range(num_sides):
    #         timmy.forward(100)
    #         timmy.right(angle)
    #
    # for shape_side_n in range(3, 11):
    #     timmy.color(random.choice(colors))
    #     draw_shape(shape_side_n)


# TODO 4: Generate a Random Walk with Random colors :
import random
# TODO 5 : Create a tuple :
import turtle as t
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# colors = ["brown", "peru", "tan", "tomato", "light salmon", "peach puff", "dark salmon"]
direction = [0, 90, 180, 270]
# augmenter la taille de stylo
timmy.pensize(15)
# modify le vitesse de la tortue
timmy.speed("fast")


for i in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))



screen = Screen()
screen.exitonclick()


import heroes
print(heroes.gen())