from tkinter import *
def event_process():
    print("이벤트 처리 되었음.....!!!!")
    
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