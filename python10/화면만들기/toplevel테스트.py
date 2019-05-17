from tkinter import *

window=Tk()
window.title("나는 제목...")
window.geometry("600x400")
window.resizable(False, False)

menubar=Menu(window)

menu_1=Menu(menubar, tearoff=0)
menu_1.add_command(label="하위 메뉴 1-1")
menu_1.add_command(label="하위 메뉴 1-2")
menu_1.add_separator()
menu_1.add_command(label="하위 메뉴 1-3")
menubar.add_cascade(label="상위 메뉴 1", menu=menu_1)

toplevel=Toplevel(window, menu=menubar)
toplevel.geometry("320x200")

label=Label(toplevel, text="나는 라벨")
label.pack()

window.mainloop()