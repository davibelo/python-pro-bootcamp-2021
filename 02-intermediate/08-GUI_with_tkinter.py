import tkinter

# creating a window object
window = tkinter.Tk()

window.title("My tkinter app")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

# calling the main loop that listener for user interaction
window.mainloop()
 