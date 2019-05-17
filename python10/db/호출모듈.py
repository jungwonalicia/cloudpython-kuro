from tkinter import *
from db import 메인모듈

w2 = None

def endCall2():
    global w2
    w2.destroy()
    메인모듈.recall()
    
def call():
    global w2
    w2 = Tk()
    b = Button(w2, text="메인으로다시 돌아가요 .", command=endCall2)
    b.pack()
    w2.mainloop()
    
    