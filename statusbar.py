import tkinter as tk

def create_statusbar(root, text):

    label = tk.Label(root, text="Words: 0")

    def update(event=None):

        words = len(text.get("1.0", "end-1c").split())

        label.config(text=f"Words: {words}")

    text.bind("<KeyRelease>", update)

    return label