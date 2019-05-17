from tkinter import *



def call(전역변수):
    w = Tk()
    print(전역변수, "값")
    b = Button(w, text="전역변수 테스트", command=call)
    b.pack()
    w.mainloop()