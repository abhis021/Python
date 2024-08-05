import tkinter as tk
import sqlite3

class App:
    def __init__(self, master):
        self.master = master
        master.geometry("1024x768")
        master.title("Sample GUI Application")

        # create a connection to the database
        self.conn = sqlite3.connect('mydatabase.db')
        self.cursor = self.conn.cursor()

        # create a table in the database
        self.cursor.execute('CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY, name TEXT)')

        # create a label to display data from the database
        self.label = tk.Label(master, text="")
        self.label.pack()

        # create a button to insert data into the database
        self.button = tk.Button(master, text="Insert", command=self.insert)
        self.button.pack()

    def insert(self):
        # insert data into the database
        self.cursor.execute('INSERT INTO mytable (name) VALUES (?)', ('John',))
        self.conn.commit()

        # display the data in the label
        self.cursor.execute('SELECT * FROM mytable')
        data = self.cursor.fetchone()
        self.label.configure(text=data[1])

    def __del__(self):
        # close the cursor and connection to the database
        self.cursor.close()
        self.conn.close()

root = tk.Tk()
app = App(root)
root.mainloop()
