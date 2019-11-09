import tkinter as tk

import pyperclip


# Utilities.

def update_clipboard():
    cliptext = pyperclip.paste()
    process_clipping(cliptext)
    root.after(ms=100, func=update_clipboard)


def clean_clip_text(cliptext):
    """Remove all characters with unicode value > 65535 (the acceptable)
    range for TCL).
    """
    return "".join(c for c in cliptext if ord(c) <= 65535)


def process_clipping(cliptext):
    cleaned = clean_clip_text(cliptext)
    label['text'] = cleaned


def on_click(label_elem):
    label_text = label_elem['text']
    print(label_text)
    pyperclip.copy(label_text)


if __name__ == '__main__':
    root = tk.Tk()

    label = tk.Label(
        root, text='', cursor='plus', relief=tk.RAISED, pady=5, wraplength=500)
    label.bind('<Button-1>',
        lambda event, label_elem=label: on_click(label_elem))
    label.pack()

    update_clipboard()

    root.mainloop()
