from tkinter import *

count = 0

root = Tk()

def Cliked():
    global count
    count += 1
    label.configure(text=count)

label = Label(root,text=0,font=('Arial',20))
label.pack()

click_button = Button(root,text='click me',font=('Arial',20),command=Cliked)
click_button.pack()

root.title('Cliker')
root.geometry('200x200')
root.mainloop()