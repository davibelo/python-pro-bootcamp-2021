from tkinter import *
# messagebox isn't a class but another module
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

DATA_FILE = "02-intermediate/13-passwordManager/data.json"

# ---------------------------- PASSWORD GENERATOR ---------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD --------------------------- #


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Empty field(s)")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"Website: {website} \nUsername: {username} \nPassword: {password} \nClick OK to save"
        )
        if is_ok:
            try:
                with open(DATA_FILE, mode="r") as data_file:
                    # reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(DATA_FILE, mode="w") as data_file:
                    # creating a data file and saving the new_data
                    json.dump(new_data, data_file, indent=4)
            else:
                # updating data with new data
                data.update(new_data)
                with open(DATA_FILE, mode="w") as data_file:
                    # saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------- #


def search():
    website = website_entry.get()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    try:
        with open(DATA_FILE, mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data to search")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, 
                message=f"username: {username}\nPassword: {password}"
                )
            username_entry.insert(0, username)
            password_entry.insert(0, password)
        # below could be used an exception handling, using raise comand
        # but it is not necessary
        # if the situation can be solved with a simple if/else, use it!
        else:
            messagebox.showerror(title="Error", message="Website is not in database")


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
website_entry = Entry(width=18)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "davibelo@gmail.com")

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

# buttons
search_button = Button(
    text="Search",
    width=14,
    font=("TkDefaultFont", 8, "normal"),
    command=search
)
search_button.grid(row=1, column=2)

generate_password_button = Button(
    text="Generate Password",
    width=14,
    font=("TkDefaultFont", 8, "normal"),
    command=generate_password
)
generate_password_button.grid(row=3, column=2)

add_button = Button(
    text="Add",
    width=38,
    font=("TkDefaultFont", 8, "normal"),
    command=save
)
add_button.grid(row=4, column=1, columnspan=2)

# mainloop
window.mainloop()
