import tkinter as tk
from tkinter import messagebox

top=tk.Tk

def helloCallBack():
    tk.messagebox.showinfo("Hello Python","Hello World")

button =tk.button(top, text = "Hello", command = helloCallBack)
button.pack()
top.mainloop()
