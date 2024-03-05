import turtle as t
import random



tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

direction = [0, 90, 180, 270]

tim.pensize(15)
tim.speed('fast')

for _ in range(200):
    tim.forward(30)
    tim.color(random_color())
    tim.setheading(random.choice(direction))










screen = t.Screen()
screen.exitonclick()