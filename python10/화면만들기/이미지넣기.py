from tkinter import *
from 화면만들기.별도의UI import *

def img_change():
    w2 = Tk()
    icon2 = PhotoImage(file = "m5.PNG")
    icon2.configure()
    label = Label(image=icon2)
    label.pack()
    w2.mainloop() 
    
if __name__ == '__main__':
    w = Tk()
    button = Button(text="나를 눌러요.....", command=img_change)
    button.pack()
    
    w.mainloop()