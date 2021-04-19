from tkinter import *

# ---------------------------- PASSWORD GENERATOR ---------------------- #

# ---------------------------- SAVE PASSWORD --------------------------- #

# ---------------------------- UI SETUP -------------------------------- #
FONT = ()

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
locker_img = PhotoImage(file="02-intermediate/13-passwordManager/logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)

username_label = Label(text="Username:")
username_label.grid(row=2, column=0)

username_entry = Entry(width=40)
username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=19)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", width=18, padx=0)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
