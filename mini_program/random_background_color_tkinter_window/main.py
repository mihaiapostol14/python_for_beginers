from tkinter import *
from tkinter import messagebox
from random import choice

"""Function for closing window"""


def Close_Window():
    if messagebox.askokcancel("Close Window", "Close Window ?"):
        MAIN_WINDOW.destroy()


"""Function generation random background color """


def random_background_color():
    color_list = [
        "#001242",
        "#20FD5B",
        "#10B1F9",
        "#FF004D",
        "#08F968",
    ]

    MAIN_WINDOW.config(background=choice(color_list))

"""Crete main window"""
MAIN_WINDOW = Tk()
MAIN_WINDOW.geometry("400x500")
MAIN_WINDOW.title("WINDOW")
MAIN_WINDOW.protocol("WM_DELETE_WINDOW", Close_Window)
MAIN_WINDOW.wm_attributes("-topmost", 1)

button = Button(text="press me", command=random_background_color)
button.pack(padx=20, pady=200)
MAIN_WINDOW.mainloop()
