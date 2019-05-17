from package_test import 모듈변수테스트
from tkinter import *

전역변수 = 100

def call():
    모듈변수테스트.call(전역변수)
    
w = Tk()
b = Button(w, text="전역변수 테스트", command=call)
b.pack()

w.mainloop()
