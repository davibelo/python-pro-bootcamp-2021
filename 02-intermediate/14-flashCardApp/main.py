from os import WEXITED
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

current_card = {}

# reading data
df = pd.read_csv("02-intermediate/14-flashCardApp/data/german_words.csv")
word_data = df.to_dict(orient="records")

# ----- GENERATE CARD ----- #


def generate_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_data)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(title_text, text="german", fill="black")
    canvas.itemconfig(word_text, text=current_card["german"], fill="black")
    flip_timer = window.after(3000, flip_card)


# ----- FLIP CARD ----- #


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(title_text, text="english", fill="white")
    canvas.itemconfig(word_text, text=current_card["english"], fill="white")


# ----- UI SETUP ----- #
window = Tk()
window.title("Flash Card App - German / English")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# canvas
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(
    file="02-intermediate/14-flashCardApp/images/card_front.png")
card_back_img = PhotoImage(
    file="02-intermediate/14-flashCardApp/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="",
                                font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="",
                               font=("Ariel", 55, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
wrong_button_img = PhotoImage(
    file="02-intermediate/14-flashCardApp/images/wrong.png")
wrong_button = Button(image=wrong_button_img,
                      highlightthickness=0, command=generate_card)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(
    file="02-intermediate/14-flashCardApp/images/right.png")
right_button = Button(image=right_button_img,
                      highlightthickness=0, command=generate_card)
right_button.grid(row=1, column=1)

generate_card()

window.mainloop()
