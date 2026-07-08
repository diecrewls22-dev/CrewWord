import tkinter as tk

from editor import create_editor
from toolbar import create_toolbar
from statusbar import create_statusbar
from file_manager import FileManager

root = tk.Tk()
root.title("CrewWord v1.1")
root.geometry("1200x800")

text = create_editor(root)

file_manager = FileManager(text)

toolbar = create_toolbar(root, file_manager, text)
toolbar.pack(fill="x")

text.pack(fill="both", expand=True)

status = create_statusbar(root, text)
status.pack(fill="x")

root.mainloop()