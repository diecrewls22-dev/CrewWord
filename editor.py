import tkinter as tk

def create_editor(root):
    frame = tk.Frame(root)

    scrollbar = tk.Scrollbar(frame)

    text = tk.Text(
        frame,
        wrap="word",
        undo=True,
        font=("Calibri", 12),
        yscrollcommand=scrollbar.set
    )

    scrollbar.config(command=text.yview)

    scrollbar.pack(side="right", fill="y")
    text.pack(fill="both", expand=True)

    frame.pack(fill="both", expand=True)

    return text