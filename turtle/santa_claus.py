import turtle


def draw_circle(t, x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
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


def draw_santa():
    screen = turtle.Screen()
    screen.bgcolor("skyblue")
    t = turtle.Turtle()
    t.speed(5)

    # Draw body
    draw_circle(t, 0, -150, 80, "red")  # Body
    draw_rectangle(t, -40, -90, 80, 50, "black")  # Belt

    # Draw head
    draw_circle(t, 0, 50, 50, "pink")  # Face

    # Draw hat
    t.penup()
    t.goto(-40, 100)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.goto(40, 100)
    t.goto(0, 170)
    t.goto(-40, 100)
    t.end_fill()
    draw_circle(t, 0, 170, 10, "white")  # Pom-pom

    # Draw eyes
    draw_circle(t, -15, 60, 5, "black")  # Left eye
    draw_circle(t, 15, 60, 5, "black")  # Right eye

    # Draw beard
    t.penup()
    t.goto(-35, 40)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.goto(-50, -10)
    t.goto(0, -30)
    t.goto(50, -10)
    t.goto(35, 40)
    t.goto(-35, 40)
    t.end_fill()

    # Draw nose
    draw_circle(t, 0, 50, 7, "pink")

    # Draw arms
    t.pensize(5)
    t.penup()
    t.goto(-80, -60)
    t.pendown()
    t.goto(-150, -100)  # Left arm
    t.penup()
    t.goto(80, -60)
    t.pendown()
    t.goto(150, -100)  # Right arm

    # Draw buttons
    draw_circle(t, 0, -100, 5, "black")
    draw_circle(t, 0, -120, 5, "black")
    draw_circle(t, 0, -140, 5, "black")

    t.hideturtle()
    screen.mainloop()


draw_santa()
