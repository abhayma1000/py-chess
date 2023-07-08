import tkinter as tk
import numpy as np
import tkmacosx
from tkinter import ttk
import math

class GraphicsManager():
    def __init__(self):
        self.window_size = [1400, 800]
        self.window_ratio = self.window_size[0] / self.window_size[1]
        
        window = tk.Tk()
        window.geometry(str(self.window_size[0]) + "x" + str(self.window_size[1]))
        window.title("Py-chess")
        # base_frame = tk.Frame().pack()
        window.resizable(width=False, height=False)

        board_frame = tk.Frame(window)
        self.buttons = self.initialize_board(board_frame)
        board_frame.pack(pady=20)


        # window.mainloop()


        return
    def initialize_board(self, window):
        square_size = 90
        counter = 1

        buttons = np.empty((8, 8), dtype=tkmacosx.Button)

        for i in range(8):
            counter -= 1
            for j in range(8):
                frame = tk.Frame(
                    master=window,
                    relief=tk.RAISED,
                    borderwidth=1,
                    bg="black",
                )
                frame.grid(row=i, column=j)

                color = "green"
                if counter % 2 == 0:
                    color = "white"

                button = tkmacosx.Button(master=frame, bg=color, highlightbackground="black", height=square_size, width = square_size)
                button.pack()
                buttons[i][j] = button

                counter += 1
        
        return buttons
        
        # label2 = tk.Label(master=frame, text=str(self.window_ratio)).pack()
    def populate_board(self, window, board):
        for i in range(8):
            for j in range(8):
                # self.buttons[i][j] SOMEOPERATION --> board[i][j].image_path
                # Want the image_path to be placed on top of that button
                return None
        

                # TODO how do I connect board to actual board

    def __str__(self):
        return "The graphics"
    def update_graphics_board(self):
        return None
        # TODO whenever a move is made, the board is updated and must be reflected on graphics
