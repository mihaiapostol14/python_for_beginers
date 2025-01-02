import turtle


def draw_circle(t, x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_snowman():
    screen = turtle.Screen()
    screen.bgcolor("skyblue")
    t = turtle.Turtle()
    t.speed(3)

    # Draw snowman body
    draw_circle(t, 0, -200, 80, "white")  # Bottom circle
    draw_circle(t, 0, -50, 60, "white")  # Middle circle
    draw_circle(t, 0, 70, 40, "white")  # Head

    # Draw eyes
    draw_circle(t, -15, 100, 5, "black")  # Left eye
    draw_circle(t, 15, 100, 5, "black")  # Right eye

    # Draw nose
    t.penup()
    t.goto(0, 90)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.goto(-10, 80)
    t.goto(10, 80)
    t.goto(0, 90)
    t.end_fill()

    # Draw buttons
    draw_circle(t, 0, 40, 5, "black")  # Top button
    draw_circle(t, 0, 10, 5, "black")  # Middle button
    draw_circle(t, 0, -20, 5, "black")  # Bottom button

    # Draw arms
    t.pensize(5)
    t.penup()
    t.goto(-50, 50)
    t.pendown()
    t.goto(-120, 70)  # Left arm
    t.penup()
    t.goto(50, 50)
    t.pendown()
    t.goto(120, 70)  # Right arm

    # Draw hat
    t.pensize(1)
    t.penup()
    t.goto(-30, 120)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    for _ in range(2):  # Hat rectangle
        t.forward(60)
        t.left(90)
        t.forward(20)
        t.left(90)
    t.end_fill()

    t.penup()
    t.goto(-40, 140)
    t.pendown()
    t.begin_fill()
    t.forward(80)  # Hat brim
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(10)
    t.end_fill()

    t.hideturtle()
    screen.mainloop()


draw_snowman()
