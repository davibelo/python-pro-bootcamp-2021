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
reps = 0
timer = None

# ------------------------- TIMER RESET --------------------------- #


def reset_timer():
    # stop the timer
    window.after_cancel(timer)
    title_label.config(text="Timer")
    # timer_text was created with canvas, so config is different
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0


# ------------------------- TIMER MECHANISM ----------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # 8th repetition
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="BREAK...", fg=RED)
    # 2, 4, 6th repetitions
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="BREAK", fg=PINK)
    # 1, 3, 5, 7th repetitions
    else:
        count_down(work_sec)
        title_label.config(text="WORK!", fg=GREEN)


# ------------------------- COUNTDOWN MECHANISM ------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # window.after method works as a timer
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # count = 0
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ------------------------- UI SETUP ------------------------------ #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN,
                    font=(FONT_NAME, 32, "bold"))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="02-intermediate/00-projects/12-pomodoroTimer/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(text="", bg=YELLOW, fg=GREEN,
                    font=(FONT_NAME, 20, "bold"))
check_marks.grid(row=3, column=1)


window.mainloop()
