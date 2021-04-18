from tkinter import *

window = Tk()
window.title("Miles to km converter")
window.minsize(width=100, height=100)
window.config(padx=10, pady=10)

entry = Entry()
entry.grid(row=0, column=1)

miles_label = Label()
miles_label.config(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label()
equal_label.config(text="is qual to:")
equal_label.grid(row=1, column=0)

result_label = Label()
result_label.config(text="Km")
result_label.grid(row=1, column=2)

calculate_button = Button()
calculate_button.config(text="Calculate")
calculate_button.grid(row=2, column=1)

window.mainloop()
