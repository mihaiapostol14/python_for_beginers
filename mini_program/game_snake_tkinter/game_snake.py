from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint

movement = 20
steps_per_sec = 10
speed = 1100 // steps_per_sec


class Snake(Canvas):
    def __init__(self):
        super().__init__(

            width=700,
            height=700,
            background='#53ff1a',
            highlightthickness=0
        )

        self.snake_pos = [(100, 80), (80, 100), (80, 100)]
        self.food_pos = self.set_new_food_pos()
        self.score = 0
        self.direction = 'Right'

        self.load_img()
        self.create_objects()

        self.bind_all('<Key>', self.on_key_press)

        self.pack()

        self.after(speed, self.perform_actions)

    def load_img(self):
        try:
            self.snake = ImageTk.PhotoImage(Image.open("sprites/player_head.png"))
            self.food = ImageTk.PhotoImage(Image.open("sprites/apple.png"))
        except IOError as error:
            ws.destroy()
            raise

    def create_objects(self):
        self.create_text(
            35,
            12,
            text=f'Score: {self.score}',
            tag='score',
            fill='black',
            font=10
        )
        for x, y in self.snake_pos:
            self.create_image(x, y, image=self.snake, tag='snake')
        self.create_image(*self.food_pos, image=self.food, tag='food')
        self.create_rectangle(
            7,
            27,
            690,
            690,
        )

    def finish_game(self):
        self.delete(ALL)
        self.create_text(self.winfo_width() / 2,
                         self.winfo_height() / 2,
                         text=f'Game over! You have scored {self.score}!',
                         fill='black',
                         font=20

                         )

    def consume_food(self):
        if self.snake_pos[0] == self.food_pos:
            self.score += 10
            self.snake_pos.append(self.snake_pos[-1])
            self.create_image(*self.snake_pos[-1], image=self.snake, tag='snake'
                              )
            self.food_pos = self.set_new_food_pos()
            self.coords(self.find_withtag("food"), self.food_pos)
            score = self.find_withtag("score")
            self.itemconfig(score, text=f'Score: {self.score}', tag='score')

    def boundry(self):
        head_x_position, head_y_position = self.snake_pos[0]

        return (
                head_x_position in (0, 700)
                or head_y_position in (20, 700)
                or (head_x_position, head_y_position) in self.snake_pos[1:]
        )

    def snake_movement(self):
        head_x_position, head_y_position = self.snake_pos[0]

        if self.direction == 'Left':
            self.new_head_position = (head_x_position - movement, head_y_position)
        elif self.direction == 'Right':
            self.new_head_position = (head_x_position + movement, head_y_position)
        elif self.direction == 'Down':
            self.new_head_position = (head_x_position, head_y_position + movement)
        elif self.direction == 'Up':
            self.new_head_position = (head_x_position, head_y_position - movement)

        self.snake_pos = [self.new_head_position] + self.snake_pos[:-1]

        for segment, position in zip(self.find_withtag('snake'), self.snake_pos):
            self.coords(segment, position)

    def on_key_press(self, e):
        new_direction = e.keysym

        all_directions = (
            'Up',
            'Down',
            'Left',
            'Right'
        )
        opposites = (
            {'Up', 'Down'},
            {'Left', 'Right'}
        )
        ws.bind_all("<KeyPress-Up>", self.on_key_press)
        ws.bind_all("<KeyPress-Down>", self.on_key_press)
        ws.bind_all("<KeyPress-Right>", self.on_key_press)
        ws.bind_all("<KeyPress-Left>", self.on_key_press)

        if (
                new_direction in all_directions
                and {new_direction, self.direction} not in opposites
        ):
            self.direction = new_direction

    def perform_actions(self):
        if self.boundry():
            self.finish_game()

        self.consume_food()
        self.snake_movement()
        self.after(speed, self.perform_actions)

    def set_new_food_pos(self):
        while True:
            x_pos = randint(1, 29) * movement
            y_pos = randint(3, 30) * movement
            food_pos = (x_pos, y_pos)
            if food_pos not in self.snake_pos:
                return food_pos


def Close_Window():
    if messagebox.askokcancel("Close Window", "Close Window ?"):
        ws.destroy()


ws = Tk()
ws.iconbitmap("icon/icon.ico")
ws.title("GAME SNAKE")
ws.protocol("WM_DELETE_WINDOW", Close_Window)
ws.wm_attributes("-topmost", 1)
ws.resizable(False, False)
board = Snake()
board.pack()

ws.mainloop()