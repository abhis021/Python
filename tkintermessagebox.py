import tkinter as tk
from tkinter import messagebox

def text_box():
    if tk.messagebox.askokcancel("Quit", "Never MInd"):
        root.destroy()

root = tk.Tk()
button = tk.Button(root, text="Press the button", command=text_box)
button.pack()
root.mainloop()
