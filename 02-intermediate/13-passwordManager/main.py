from tkinter import *

# ---------------------------- PASSWORD GENERATOR ---------------------- #

# ---------------------------- SAVE PASSWORD --------------------------- #

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()    
    with open("02-intermediate/13-passwordManager/data.txt", mode="a") as file:
        file.write(f"\n{website} | {username} | {password}")

# ---------------------------- UI SETUP -------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

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
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "davibelo@gmail.com")
password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

# buttons
generate_password_button = Button(
    text="Generate Password", width=14, font=("TkDefaultFont", 8, "normal"))
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=38, font=("TkDefaultFont", 8, "normal"), command=save)
add_button.grid(row=4, column=1, columnspan=2)


# mainloop
window.mainloop()
