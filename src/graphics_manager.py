import tkinter as tk
import numpy as np
import tkmacosx
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import math


class GraphicsManager():
    def __init__(self, board):
        self.window_size = [760] * 2
        self.window_ratio = self.window_size[0] / self.window_size[1]
        
        self.window = tk.Tk()
        self.window.geometry(str(self.window_size[0]) + "x" + str(self.window_size[1]))
        self.window.title("Py-chess")
        self.window.resizable(width=False, height=False)

        self.board_frame = tk.Frame(self.window)
        self.board_frame.grid(pady=20, padx=20)
        self.buttons = self.initialize_board(board)

        return

    def initialize_board(self, board: np.array):
        self.square_size = 90
        counter = 1

        buttons = np.empty((8, 8), dtype=tkmacosx.Button)

        self.color_map = np.empty((8, 8), dtype=str)

        for i in range(8):
            counter -= 1
            for j in range(8):

                color = "green"
                if counter % 2 == 0:
                    color = "white"
                self.color_map[i][j] = color

                if board[i][j] != None:
                    image1 = PhotoImage(file=board[i][j].image_path)
                    button = tkmacosx.Button(master=self.board_frame, bg=color, highlightbackground="black", height=self.square_size, width = self.square_size, image=image1)
                else:
                    button = tkmacosx.Button(master=self.board_frame, bg=color, highlightbackground="black", height=self.square_size, width = self.square_size)
                button.grid(row=i, column=j)
                buttons[i][j] = button

                counter += 1
        
        return buttons
    
    def get_actual_color(self, short: str):
        if short == "g":
            return "green"
        
        if short == "w":
            return "white"
    
    def update_board(self, board: np.array):
        self.buttons = self.initialize_board(board)

    def __str__(self):
        return "The graphics"
    def update_graphics_board(self):
        return None
        # TODO whenever a move is made, the board is updated and must be reflected on graphics
