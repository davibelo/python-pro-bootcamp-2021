from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    result_label.config(text=str(km))

window = Tk()
window.title("Miles to km converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is qual to:")
equal_label.grid(row=1, column=0)

result_label = Label(text=0)
result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
