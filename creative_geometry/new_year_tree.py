import turtle


def draw_triangle(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()


def draw_rectangle(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def draw_star(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


def draw_christmas_tree():
    screen = turtle.Screen()
    screen.bgcolor("skyblue")
    t = turtle.Turtle()
    t.speed(5)

    # Draw tree trunk
    draw_rectangle(t, -20, -150, 40, 60, "brown")

    # Draw tree layers
    draw_triangle(t, -100, -90, 200, "green")  # Bottom layer
    draw_triangle(t, -80, 20, 160, "green")  # Middle layer
    draw_triangle(t, -60, 110, 120, "green")  # Top layer

    # Draw star on top
    draw_star(t, 0, 160, 30, "yellow")

    # Draw ornaments
    t.penup()
    t.goto(-70, 40)
    t.pendown()
    t.dot(20, "red")

    t.penup()
    t.goto(50, 60)
    t.pendown()
    t.dot(20, "blue")

    t.penup()
    t.goto(-40, 100)
    t.pendown()
    t.dot(20, "gold")

    t.penup()
    t.goto(-10, 100)
    t.pendown()
    t.dot(20, "gold")

    t.hideturtle()
    screen.mainloop()


draw_christmas_tree()
