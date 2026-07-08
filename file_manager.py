from tkinter import filedialog
import tkinter as tk

class FileManager:

    def __init__(self, text):
        self.text = text

    def new(self):
        self.text.delete("1.0", tk.END)

    def open(self):
        file = filedialog.askopenfilename(
            filetypes=[("CrewWord Documents", "*.cwd")]
        )

        if file:
            with open(file, "r", encoding="utf-8") as f:
                self.text.delete("1.0", tk.END)
                self.text.insert("1.0", f.read())

    def save(self):
        file = filedialog.asksaveasfilename(
            defaultextension=".cwd",
            filetypes=[("CrewWord Documents", "*.cwd")]
        )

        if file:
            with open(file, "w", encoding="utf-8") as f:
                f.write(self.text.get("1.0", tk.END))