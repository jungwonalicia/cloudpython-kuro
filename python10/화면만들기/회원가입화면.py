from tkinter import *
from db.DB연결테스트 import *

w = Tk()
w.geometry("600x300")
w.title("나는 회원가입하는 화면...")
l1 = Label(w, text="아이디")
l1.pack()
l2 = Label(w, text="비밀번호")
l2.pack()
l3 = Label(w, text="이름")
l3.pack()
l4 = Label(w, text="전화번호")
l4.pack()

w.mainloop() 