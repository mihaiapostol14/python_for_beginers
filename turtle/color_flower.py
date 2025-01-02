from turtle import *
from colorsys import *

tracer(7)

bgcolor('black')
for j in range(36):
    h = j / 36

    color(hsv_to_rgb(h, 0.8, 1))

    begin_fill()

    for i in range(2):
        circle(140, 90)
        left(90)
        circle(140, 90)
        left(90)
    end_fill()
    right(10)
done()
