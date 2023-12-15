import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


root = tk.Tk()
root.title("ScrolledText Widget")


st = ScrolledText(root, width=50,  height=10)
st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

root.mainloop()
from lib import *


def return_pressed(event):
    win=tk.Tk()
    win.mainloop()
    print("hello")


root = tk.Tk()

btn = ttk.Label(root, text=listDatabases())
btn.bind('<Button-1>', return_pressed)
# a=tk.Label(root,text=b).pack()


btn.focus()
btn.pack()
a=tk.Label(root,text="").pack()

root.mainloop()