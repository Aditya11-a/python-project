import tkinter as  tk
from tkinter import ttk
import customtkinter as ctk
from tkinter.messagebox import showerror,showinfo
from lib import *
from idlelib.tooltip import Hovertip

def createdb(event):
    def hg (event):
        dbName=ent2.get()
        print(dbName)
        createDatabase(dbName)
        def jk(event):
            root.deiconify()
            root1.withdraw()
            root2.withdraw()
        root2=ctk.CTkToplevel(root1)
        root2.geometry("150x100")
        root2.config(bg="black")
        root2.title("DB Created")
        lb3 = ctk.CTkLabel(root2,text="Database Created",bg_color="black",text_color="white")
        ent3 = ctk.CTkButton(root2,text="Ok",width=10,bg_color="black")
        ent3.bind('<Button-1>',jk)
        lb3.place(x=20,y=20)
        ent3.place(x=60,y=50)
        

    root.withdraw()
    root1=ctk.CTkToplevel(root)
    root1.config(bg="black")
    root1.title("createdb")
    root1.geometry("200x150")
    ent2=ctk.CTkEntry(root1,bg_color="black",text_color="white",width=100)
    tip1 = Hovertip(ent2,"Do not enter any special\ncharacter except ( _ ) ")
    btn2=ctk.CTkButton(root1,bg_color="black",text="Create",text_color="white",width=10)
    btn2.bind('<Button-1>',hg)

    ent2.place(x=50,y=45)
    btn2.place(x=75,y=90)
    
def mainwin(event):
    root.withdraw()
    dbName=ent1.get()
    print(dbName)
    selectDatabase(dbName)
    root4 = ctk.CTkToplevel()
    root4.title(dbName)
    root4.geometry('1000x500')
    
    
    

root= ctk.CTk()
root.geometry('500x300')
root.config(bg="black")



def  jh(event):
    dbName=ent1.get()
    print(dbName)
    selectDatabase(dbName)


a= ctk.Variable(value=listDatabases())
lb1 = ctk.CTkLabel(root,text="Select Database:",text_color="white",bg_color="black")
lb2 = ctk.CTkLabel(root,text="Select Database:",text_color="white",bg_color="black")
ent1 = ctk.CTkComboBox(
    root,bg_color="black",text_color="white",values=a.get(),hover=True,dropdown_fg_color="white",button_color="black",border_color="black")
ent1.set(value="Select Databases")
lb2 = ctk.CTkLabel(root,text="Want to make a new one?",bg_color="black",text_color="blue")
lb2.bind('<Button-1>',createdb)
btn1 = ctk.CTkButton(root,text="Use",bg_color="black",text_color="white",border_width=None)
btn1.bind('<Button-1>',mainwin)






lb1.place(x=170,y=80)
lb2.place(x=170,y=250)
ent1.place(x=168,y=100)
btn1.place(x=170,y=150)











root.mainloop()