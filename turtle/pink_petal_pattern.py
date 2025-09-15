import turtle as t

t.speed(0)
t.bgcolor("black")
colors = ["#ff00ff", "#ff69b4", "#ff1493", "#c71585"]

for i in range(36):
    t.color(colors[i % 4])
    t.begin_fill()
    t.circle(250, 60)
    t.left(120)
    t.end_fill()
    t.left(10)

t.color("yellow")
t.hideturtle()
t.done()