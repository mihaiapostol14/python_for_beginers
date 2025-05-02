import turtle


def multi_colored_spiral_overlapping_circles():
    screen = turtle.Screen()
    screen.bgcolor("black")

    my_turtle = turtle.Turtle()
    my_turtle.speed(0)

    colors = ["blue", "white", "orange", "pink"]

    for _ in range(36):
        my_turtle.pencolor(colors[_ % 4])
        my_turtle.circle(100)
        my_turtle.left(10)

    my_turtle.hideturtle()
    screen.exitonclick()


multi_colored_spiral_overlapping_circles()