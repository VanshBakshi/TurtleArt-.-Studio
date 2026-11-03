"""
Pentagon Flower — TurtleArt Studio
Category: Geometric Art
Run: python p007.py
Requires: Python 3 (turtle is included in the standard library)
"""
import turtle
import math
import colorsys

screen = turtle.Screen()
screen.setup(900, 700)
screen.bgcolor("#101426")
screen.title("Pentagon Flower | TurtleArt Studio")
screen.colormode(255)

artist = turtle.Turtle()
artist.speed(0)
artist.pensize(2)
artist.hideturtle()

def color(i, total=120):
    r, g, b = colorsys.hsv_to_rgb((i / max(total, 1)) % 1, 0.78, 1)
    return int(r * 255), int(g * 255), int(b * 255)

artist.penup()
artist.goto(0, 0)
artist.pendown()

# The pattern uses a repeatable seed so every run produces the same artwork.
if "geometric" in ("geometric", "festival", "advanced"):
    for i in range(180):
        artist.pencolor(color(i, 180))
        artist.forward(3 + i * 1.35)
        artist.left(59 + (i % 7) * 2)
        if i % 6 == 0:
            artist.circle(18 + i * 0.18, 90)
elif "geometric" in ("spiral", "math"):
    for i in range(720):
        artist.pencolor(color(i, 720))
        artist.forward(0.35 + i * 0.22)
        artist.left(91 if i % 2 else 89)
        artist.circle(22 + (i % 90) * 0.35, 18)
elif "geometric" in ("flower", "mandala"):
    for ring in range(5):
        artist.pencolor(color(ring * 22, 120))
        for petal in range(24):
            artist.circle(45 + ring * 13, 60)
            artist.left(120)
            artist.circle(45 + ring * 13, 60)
            artist.left(15)
        artist.right(18)
elif "geometric" == "fractal":
    def branch(length, depth):
        if depth == 0:
            return
        artist.pencolor(color(depth * 17, 100))
        artist.forward(length)
        artist.left(28)
        branch(length * 0.72, depth - 1)
        artist.right(56)
        branch(length * 0.72, depth - 1)
        artist.left(28)
        artist.backward(length)
    artist.left(90)
    artist.penup()
    artist.goto(0, -260)
    artist.pendown()
    branch(115, 8)
elif "geometric" == "nature":
    artist.left(65)
    for i in range(90):
        artist.pencolor(color(i, 90))
        artist.forward(4 + i * 1.2)
        artist.right(38)
        artist.circle(18 + (i % 12) * 2, 70)
else:
    for i in range(240):
        artist.pencolor(color(i, 240))
        artist.circle(70 + (i % 35) * 2, 45)
        artist.left(137)
        artist.forward(2 + i * 0.8)

screen.exitonclick()
