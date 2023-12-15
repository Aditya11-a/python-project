import tkinter as  tk
from tkinter import ttk
from lib import *
from tkinter.scrolledtext import ScrolledText as st


root= tk.Tk()
root.geometry('500x400')
root.config(bg="black")

stb = st.ScrolledText(root, width= 30, height=30,text=listDatabases())
stb.pack(expand=True)



root.mainloop()