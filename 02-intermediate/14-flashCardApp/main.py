from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"




# ---- UI ---- #

window = Tk()
window.title("Flash Card App - German / English")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(
    file="02-intermediate/14-flashCardApp/images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
#                                 font=(FONT_NAME, 24, "bold"))
# canvas.grid(row=1, column=1)





window.mainloop()
