#code by abhis021@github
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("600x400")

        # Create a text area
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH)

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Add file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Add options to the file menu
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)

    def new_file(self):
        """Create a new file"""
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        """Open an existing file"""
        file_path = filedialog.askopenfilename(defaultextension=".txt", 
                                                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.text_area.delete(1.0, tk.END)  # Clear current text area
            with open(file_path, 'r') as file:
                self.text_area.insert(tk.END, file.read())  # Read and insert the file content

    def save_file(self):
        """Save the current file"""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                   filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))  # Write the text area content to file

    def exit_app(self):
        """Exit the application"""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
