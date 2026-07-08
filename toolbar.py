import tkinter as tk

def create_toolbar(root, file_manager, text):

    toolbar = tk.Frame(root)

    tk.Button(toolbar, text="New", command=file_manager.new).pack(side="left")

    tk.Button(toolbar, text="Open", command=file_manager.open).pack(side="left")

    tk.Button(toolbar, text="Save", command=file_manager.save).pack(side="left")

    return toolbar