from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo

w = Tk()
icon = PhotoImage(file="web.png")

label = Label(w, image=icon)
label.pack()

messagebox.showinfo("여기는..뭐야..", "여기는 출력이지...")
showinfo("여기는..뭐야..", "여기는 또 출력이지...")
w.mainloop()