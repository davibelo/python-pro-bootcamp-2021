from tkinter import *
import math

# -------------------------- CONSTANTS ---------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ------------------------- TIMER RESET --------------------------- #

# ------------------------- TIMER MECHANISM ----------------------- #


def start_timer():
    count_down(5*60)

# ------------------------- COUNTDOWN MECHANISM ------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ------------------------- UI SETUP ------------------------------ #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN,
                    font=(FONT_NAME, 32, "bold"))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="02-intermediate/12-pomodoroTimer/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset")
reset_button.grid(row=2, column=2)

check_marks = Label(text="✔✔", bg=YELLOW, fg=GREEN,
                    font=(FONT_NAME, 20, "bold"))
check_marks.grid(row=3, column=1)


window.mainloop()