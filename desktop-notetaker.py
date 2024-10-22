# import tkinter as tk
# from tkinter import filedialog, messagebox

# class Notepad:
#     def __init__(self, root):
#         self.root = root
#         self.text_area = tk.Text(self.root)
#         self.text_area.pack(fill="both", expand=True)

#         # Syntax highlighting rules for Python
#         self.highlighting_rules = {
#             r"\b(if|else if|elif|for|while)\b": ("red",),
#             r"\b(True|False)\b": ("blue",),
#             r"\b([a-zA-Z_][a-zA-Z0-9_]*)\b": ("blue",),
#             r'"[^\"]*"' : ("green",),
#             r"'\([^)]*\)'": ("red",),
#             r"\d+": ("black",),
#         }

#         # Bind the highlight function to key press events
#         self.text_area.tag_config("highlighted", foreground="white")
#         self.text_area.config(highlightbackground=self.get_highlight_color)

#         # Menu creation
#         self.create_menu()

#     def new_file(self):
#         self.text_area.delete(1.0, tk.END)

#     def open_file(self):
#         filename = filedialog.askopenfilename(
#             defaultextension=".txt",
#             filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
#         )
#         if filename:
#             try:
#                 with open(filename, "r") as file:
#                     self.text_area.delete(1.0, tk.END)
#                     for line in file:
#                         self.text_area.insert(tk.END, line + "\n")
#             except Exception as e:
#                 messagebox.showerror("Error", str(e))

#     def save_file(self):
#         filename = filedialog.asksaveasfilename(
#             defaultextension=".txt",
#             filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
#         )
#         if filename:
#             try:
#                 with open(filename, "w") as file:
#                     for line in self.text_area.get(1.0, tk.END).splitlines():
#                         file.write(line + "\n")
#             except Exception as e:
#                 messagebox.showerror("Error", str(e))

#     def save_as_file(self):
#         self.save_file()

#     def page_setup(self):
#         print("Page setup")

#     def print_file(self):
#         print("Printing")

#     def exit(self):
#         self.root.destroy()

#     def undo(self):
#         self.text_area.edit_undo()

#     def cut(self):
#         self.text_area.clipboard_clear()
#         self.text_area.clipboard_append(self.text_area.selection_get())
#         self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)

#     def copy(self):
#         self.text_area.clipboard_clear()
#         self.text_area.clipboard_append(self.text_area.selection_get())

#     def paste(self):
#         self.text_area.insert(tk.INSERT, self.text_area.clipboard_get())

#     def delete(self):
#         self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)

#     def find(self):
#         filename = filedialog.askopenfilename(
#             defaultextension=".txt",
#             filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
#         )
#         if filename:
#             try:
#                 with open(filename, "r") as file:
#                     self.text_area.delete(1.0, tk.END)
#                     for line in file:
#                         self.text_area.insert(tk.END, line + "\n")
#             except Exception as e:
#                 messagebox.showerror("Error", str(e))

#     def find_next(self):
#         content = self.text_area.get(1.0, tk.END)
#         start_pos = 0
#         while True:
#             start_pos = content.find(next, start_pos)
#             if start_pos == -1:
#                 break
#             end_pos = start_pos + len(next) - 1
#             content = content[:start_pos] + '\033[3m' + next + '\033[0m' + content[end_pos+1:]
#             self.text_area.tag_add("highlight", f"{start_pos}-{end_pos}", f"{end_pos}-{start_pos}")
#         for tag in self.text_area.tag_names():
#             if tag != "highlight":
#                 self.text_area.tag_delete(tag)

#         next = input()
#         self.find_next()

#     def find_previous(self):
#         content = self.text_area.get(1.0, tk.END)
#         start_pos = 0
#         while True:
#             start_pos = content.find(previous, start_pos)
#             if start_pos == -1:
#                 break
#             end_pos = start_pos + len(previous) - 1
#             content = content[:start_pos] + '\033[3m' + previous + '\033[0m' + content[end_pos+1:]
#             self.text_area.tag_add("highlight", f"{start_pos}-{end_pos}", f"{end_pos}-{start_pos}")
#         for tag in self.text_area.tag_names():
#             if tag != "highlight":
#                 self.text_area.tag_delete(tag)

#         previous = input()
#         self.find_previous()

#     def replace(self):
#         filename = filedialog.askopenfilename(
#             defaultextension=".txt",
#             filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
#         )
#         if filename:
#             try:
#                 with open(filename, "r") as file:
#                     new_content = file.read()
#                     self.text_area.delete(1.0, tk.END)
#                     for line in new_content.splitlines():
#                         self.text_area.insert(tk.END, line + "\n")
#             except Exception as e:
#                 messagebox.showerror("Error", str(e))

#     def goto(self):
#         filename = filedialog.askopenfilename(
#             defaultextension=".txt",
#             filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
#         )
#         if filename:
#             try:
#                 with open(filename, "r") as file:
#                     self.text_area.delete(1.0, tk.END)
#                     for line in file:
#                         self.text_area.insert(tk.END, line + "\n")
#             except Exception as e:
#                 messagebox.showerror("Error", str(e))

#     def create_menu(self):
#         menubar = self.root.menuBar()
#         filemenu = menubar.addMenu("File")
#         editmenu = menubar.addMenu("Edit")
#         viewmenu = menubar.addMenu("View")

#         filemenu.add_command(label="New", accelerator='Ctrl+N', command=self.new_file)
#         filemenu.add_command(label="Open...", accelerator='Ctrl+O', command=self.open_file)
#         filemenu.add_command(label="Save", accelerator='Ctrl+S', command=self.save_file)
#         filemenu.add_command(label="Save As...", accelerator='Ctrl+Shift+S', command=self.save_as_file)

#         editmenu.add_command(label="Cut", accelerator='Ctrl+C', command=self.cut)
#         editmenu.add_command(label="Copy", accelerator='Ctrl+V', command=self.copy)
#         editmenu.add_command(label="Paste", accelerator='Ctrl+X', command=self.paste)
#         editmenu.add_command(label="Delete", accelerator='Del', command=self.delete)

#         viewmenu.add_command(label="Find...", accelerator='Ctrl+F', command=self.find)
#         viewmenu.add_command(label="Find Next", accelerator='F3', command=self.find_next)
#         viewmenu.add_command(label="Find Previous", accelerator='Shift+F3', command=self.find_previous)
#         viewmenu.add_command(label="Replace...", accelerator='Ctrl+H', command=self.replace)
#         viewmenu.add_command(label="Go To", accelerator='Ctrl+G', command=self.goto)

#         menubar.addSeparator()

#         filemenu.add_command(label="Page Setup", accelerator='Ctrl+Shift+P', command=self.page_setup)
#         filemenu.add_command(label="Print...", accelerator='Ctrl+P', command=self.print_file)
#         filemenu.add_separator()
#         filemenu.add_command(label="Exit", accelerator='Alt+F4', command=self.exit)

#         editmenu.add_command(label="Undo", accelerator='Ctrl+Z', command=self.undo)

#         viewmenu.add_command(label="Go To", accelerator='Ctrl+G', command=self.goto)


#     def get_color(self):
#         return '#0000ff'

# def main():
#     app = Application()
#     app.title('Text Editor')
#     app.run()

# class Application(QApplication):
#     def __init__(self):
#         super().__init__(['text_editor'])
#         self.create_menu()

# if __name__ == "__main__":
#     main()


import sys
from PyQt5.QtWidgets import QApplication, QMenuBar, QMenu, QAction, QTextEdit, QMessageBox
from PyQt5.QtGui import QFont

class Notepad:
    def __init__(self, root):
        self.root = root
        self.text_area = QTextEdit(self.root)
        self.text_area.setPlainText("Enter your text here.")
        self.text_area.setFont(QFont('Arial', 12))

        menubar = QMenuBar()
        filemenu = menubar.addMenu("File")
        editmenu = menubar.addMenu("Edit")
        viewmenu = menubar.addMenu("View")

        new_action = QAction('New', self.root)
        open_action = QAction('Open...', self.root)
        save_action = QAction('Save', self.root)
        save_as_action = QAction('Save As...', self.root)

        filemenu.addAction(new_action)
        filemenu.addAction(open_action)
        filemenu.addAction(save_action)
        filemenu.addAction(save_as_action)

        editmenu.addAction(QAction('Cut', self.root))
        editmenu.addAction(QAction('Copy', self.root))
        editmenu.addAction(QAction('Paste', self.root))

        viewmenu.addAction(QAction('Find...', self.root))
        viewmenu.addAction(QAction('Find Next', self.root))
        viewmenu.addAction(QAction('Find Previous', self.root))
        viewmenu.addAction(QAction('Replace...', self.root))

        menubar.addMenu(filemenu)
        menubar.addMenu(editmenu)
        menubar.addMenu(viewmenu)

    def run(self):
        self.root.show()
        sys.exit(self.root.exec_())

class Application:
    def __init__(self):
        app = QApplication(sys.argv)
        window = QWidget()
        layout = QVBoxLayout()
        notepad = Notepad(window)
        layout.addWidget(notepad.text_area)
        window.setLayout(layout)

if __name__ == "__main__":
    app = Application()
    app.run()