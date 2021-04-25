from tkinter import *
import os

import pandas

THEME_COLOR = "#375362"

REL_PATH = "02-intermediate/19-TriviaQuizApp/"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.score_label = Label(text=" Score:0",
                                 fg="white",
                                 bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250,
                             bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            text="test",
            font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        true_img = PhotoImage(
            file=f"{REL_PATH}images/true.png")
        self.true_button = Button(
            image=true_img, highlightthickness=0)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        false_img = PhotoImage(
            file=f"{REL_PATH}images/false.png")
        self.false_button = Button(
            image=false_img, highlightthickness=0)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)
        self.window.mainloop()
