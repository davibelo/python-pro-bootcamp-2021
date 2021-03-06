from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

current_card = {}

# ----- READING WORD DATA ----- #

try:
    df = pd.read_csv("03-projects-GUI/12-flashCard/data/to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("03-projects-GUI/12-flashCard/data/all_words.csv")
finally:
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

# ----- IS KNOWN LOGIC ----- #


def is_known():
    word_data.remove(current_card)
    df_to_learn = pd.DataFrame.from_records(word_data)
    df_to_learn.to_csv("03-projects-GUI/12-flashCard/data/to_learn.csv",
                       index=False)
    generate_card()


# ----- UI SETUP ----- #
window = Tk()
window.title("Flash Card App - German / English")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# canvas
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(
    file="03-projects-GUI/12-flashCard/images/card_front.png")
card_back_img = PhotoImage(
    file="03-projects-GUI/12-flashCard/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="",
                                font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="",
                               font=("Ariel", 55, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
wrong_button_img = PhotoImage(
    file="03-projects-GUI/12-flashCard/images/wrong.png")
wrong_button = Button(image=wrong_button_img,
                      highlightthickness=0, command=generate_card)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(
    file="03-projects-GUI/12-flashCard/images/right.png")
right_button = Button(image=right_button_img,
                      highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

generate_card()

window.mainloop()
