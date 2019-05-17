from tkinter import *
from db.DB연결테스트 import *

def event_process():
    print("이벤트 처리 되었음.....!!!!")
    id = id_input.get()
    pw = pw_input.get()
    name = name_input.get()
    tel = tel_input.get()
    db_insert(id, pw, name, tel)
#     print("당신이 입력한 id: ", id)

if __name__ == '__main__':
    w = Tk()
    w.geometry("500x450")
    w.title("나의 첫 윈도우")
    w.configure(bg="pink")
    
    id_text = Label(w, text="아이디 입력", font=("궁서", 30), fg="blue", bg="pink")
    pw_text = Label(w, text="패스워드 입력", font=("궁서", 30), fg="blue", bg="pink")
    name_text = Label(w, text="이름 입력", font=("궁서", 30), fg="blue", bg="pink")
    tel_text = Label(w, text="전화번호 입력", font=("궁서", 30), fg="blue", bg="pink")
    insert = Button(w, text="회원가입 처리", font=("궁서", 30), fg="red", bg="yellow", command=event_process)
    
    id_input = Entry(w, font=("궁서", 30), fg="red", bg="yellow", width=12)
    pw_input = Entry(w, font=("궁서", 30), fg="red", bg="yellow", width=12)
    name_input = Entry(w, font=("궁서", 30), fg="red", bg="yellow", width=12)
    tel_input = Entry(w, font=("궁서", 30), fg="red", bg="yellow", width=12)
    
    id_text.pack()
    id_input.pack()
    pw_text.pack()
    pw_input.pack()
    name_text.pack()
    name_input.pack()
    tel_text.pack()
    tel_input.pack()
    insert.pack()
    w.mainloop()