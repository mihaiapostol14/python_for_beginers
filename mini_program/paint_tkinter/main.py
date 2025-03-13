import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Paint")

canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

last_x, last_y = None, None
color = "black"

brush_size = 5
def paint(event):
    global last_x, last_y
    if last_x and last_y:
        canvas.create_line(last_x, last_y, event.x, event.y, width=brush_size, fill=color, capstyle=tk.ROUND, smooth=tk.TRUE)
    last_x, last_y = event.x, event.y

def reset(event):
    global last_x, last_y
    last_x, last_y = None, None

def choose_color():
    global color
    color_code = colorchooser.askcolor(title="Выберите цвет")[1]
    if color_code:
        color = color_code

def change_brush_size(val):
    global brush_size
    brush_size = int(val)

canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", reset)

tk.Button(root, text="Выбрать цвет", command=choose_color).pack()
tk.Scale(root, from_=1, to_=20, orient=tk.HORIZONTAL, label="Brush Size", command=change_brush_size).pack()

root.mainloop()