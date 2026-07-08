import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("CrewWord v1.0")
root.geometry("1000x700")

text = tk.Text(root, wrap="word", font=("Calibri", 12))
text.pack(fill="both", expand=True)

def new_file():
    text.delete("1.0", tk.END)

def open_file():
    file = filedialog.askopenfilename(filetypes=[("CrewWord Documents", "*.cwd")])
    if file:
        with open(file, "r", encoding="utf-8") as f:
            text.delete("1.0", tk.END)
            text.insert("1.0", f.read())

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".cwd", filetypes=[("CrewWord Documents", "*.cwd")])
    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", tk.END))

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()