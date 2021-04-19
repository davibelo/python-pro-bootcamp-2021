from tkinter import *

# ---------------------------- PASSWORD GENERATOR ---------------------- #

# ---------------------------- SAVE PASSWORD --------------------------- #

# ---------------------------- UI SETUP -------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
locker_img = PhotoImage(file="02-intermediate/13-passwordManager/logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(row=0, column=0, columnspan=3)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

# buttons
generate_password_button = Button(
    text="Generate Password", width=17, font=("Arial", 8, "normal"))
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=43, font=("Arial", 8, "normal"))
add_button.grid(row=4, column=1, columnspan=2)

# mainloop
window.mainloop()
