import turtle
import colorsys


def draw_flower():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    turtle.colormode(255)

    num_colors = 36
    colors = [colorsys.hsv_to_rgb(i / num_colors, 1.0, 1.0) for i in range(num_colors)]
    colors = [(int(r * 255), int(g * 255), int(b * 255)) for r, g, b in colors]

    for i in range(72):
        t.pencolor(colors[i % num_colors])
        t.circle(100)
        t.right(360 / 72 + 5)
        t.forward(10)

    t.hideturtle()
    screen.mainloop()


draw_flower()
