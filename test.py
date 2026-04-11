# import tkinter as tk
from tkinter import *

root = Tk()
root.title("Main Menu")
root.geometry("300x300")

label = Label(root, text='Hello, im Me!', font=('Arial', 18))
label.pack(pady=20)

# Create a button widget
def on_click():
    label.config(text="Button Clicked!")

button = Button(root, text="Click Me", command=on_click)
button.pack()

# Start the Tkinter event loop
root.mainloop()