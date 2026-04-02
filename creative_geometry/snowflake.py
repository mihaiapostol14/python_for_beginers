import turtle


def draw_snowflake_branch(t, length, level):
    if level == 0:
        t.forward(length)
        return
    length /= 3.0
    draw_snowflake_branch(t, length, level - 1)
    t.left(60)
    draw_snowflake_branch(t, length, level - 1)
    t.right(120)
    draw_snowflake_branch(t, length, level - 1)
    t.left(60)
    draw_snowflake_branch(t, length, level - 1)


def draw_snowflake():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.color("white")
    t.penup()
    t.goto(-150, 100)
    t.pendown()

    for _ in range(3):  # Draw three branches of the snowflake
        draw_snowflake_branch(t, 300, 4)
        t.right(120)

    t.hideturtle()
    screen.mainloop()


draw_snowflake()
