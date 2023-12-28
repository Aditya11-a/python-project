import tkinter as tk
import customtkinter as ctk
def f():
    print(b.get())
root = ctk.CTk()
b = ctk.CTkEntry(root)
c = ctk.CTkButton(root,command=f)
b. pack()
c.pack()

root.mainloop()
