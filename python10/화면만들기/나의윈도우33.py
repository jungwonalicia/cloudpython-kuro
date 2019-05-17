from tkinter import *
from db.DB연결테스트 import *

record, id_input, pw_input, name_input, tel_input, data, result, count = None, None, None, None, None, None, None, 0
id_result = [None] * 15

def select_process():
    global data, record
    print("정보 검색 시작..")
    id = data.get()
    record = db_select(id)  
    select_result_ui(record)
    
def select_process2():
    global id_result, record, count
    print("정보 검색 시작..")
    id = id_result[count]['text']
    record = db_select(id)  
    select_result_ui(record)
    
def select_all_process():
    global result
    print("정보 검색 시작..")
    result = db_select_all()  
    select_all_ui(result)
    
def select_all_process2():
    global result
    print("정보 검색 시작..")
    result = db_select_all()  
    select_all_ui2(result)
    
def select_all_process3():
    global result
    print("정보 검색 시작..")
    result = db_select_all()  
    select_all_ui3(result)
    
def select_all_process4():
    global result
    print("정보 검색 시작..")
    result = db_select_all()  
    select_all_ui4(result)
    
def event_process():
    print("이벤트 처리 되었음.....!!!!")
    id = id_input.get()
    pw = pw_input.get()
    name = name_input.get()
    tel = tel_input.get()
    db_insert(id, pw, name, tel)
#     print("당신이 입력한 id: ", id)


def delete_ui():
    pass
def update_ui():
    pass

def select_ui():
    global data
    w = Tk()
    w.geometry("300x200")
    w.title("나의 첫 윈도우")
    w.configure(bg="pink")
    intro = Label(w, text="검색할 ID", font=("궁서", 30), fg="blue", bg="pink")
    data = Entry(w, font=("궁서", 30), fg="red", bg="yellow", width=12)
    start = Button(w, text="회원정보 검색", font=("궁서", 20), fg="red", bg="yellow", command=select_process)
    
    intro.pack()
    data.pack()
    start.pack()
    w.mainloop()

    
def select_all_ui(result):
    global id_input, pw_input, name_input, tel_input
    w = Tk()
    w.geometry("500x500")
    w.title("나의 첫 윈도우")
    w.configure(bg="pink")
    
    id_text = Label(w, text="아이디 ", font=("궁서", 30), fg="blue", bg="pink")
    pw_text = Label(w, text="패스워드", font=("궁서", 30), fg="blue", bg="pink")
    name_text = Label(w, text="이름", font=("궁서", 30), fg="blue", bg="pink")
    tel_text = Label(w, text="전화번호", font=("궁서", 30), fg="blue", bg="pink")
    id_text.pack()
    pw_text.pack()
    name_text.pack()
    tel_text.pack()
    
    
    for record in result:
        id_input = Label(w, text=record[0], font=("궁서", 30), fg="blue", bg="yellow")
        pw_input = Label(w, text=record[1], font=("궁서", 30), fg="blue", bg="yellow")
        name_input = Label(w, text=record[2], font=("궁서", 30), fg="blue", bg="yellow")
        tel_input = Label(w, text=record[3], font=("궁서", 30), fg="blue", bg="yellow")
        id_input.pack()
        pw_input.pack()
        name_input.pack()
        tel_input.pack()


    w.mainloop()
    
    
def select_all_ui2(result):
    global id_input, pw_input, name_input, tel_input
    w = Tk()
    w.geometry("700x700")
    w.title("나의 첫 윈도우")
    w.configure(bg="pink")
    
    id_text = Label(w, text="아이디 ", font=("궁서", 30), fg="blue", bg="pink")
    pw_text = Label(w, text="패스워드", font=("궁서", 30), fg="blue", bg="pink")
    name_text = Label(w, text="이름", font=("궁서", 30), fg="blue", bg="pink")
    tel_text = Label(w, text="전화번호", font=("궁서", 30), fg="blue", bg="pink")
    id_text.grid(row= 0, column = 0)
    pw_text.grid(row= 0, column = 1)
    name_text.grid(row= 0, column = 2)
    tel_text.grid(row= 0, column = 3)
    
    size = len(result)
    print(size)
    start = 1
    for record in result:
        if start == size:
            break
        id_input = Label(w, text=record[0], font=("궁서", 30), fg="blue", bg="yellow")
        pw_input = Label(w, text=record[1], font=("궁서", 30), fg="blue", bg="yellow")
        name_input = Label(w, text=record[2], font=("궁서", 30), fg="blue", bg="yellow")
        tel_input = Label(w, text=record[3], font=("궁서", 30), fg="blue", bg="yellow")
        id_input.grid(row= start, column = 0)
        pw_input.grid(row= start, column = 1)
        name_input.grid(row= start, column = 2)
        tel_input.grid(row= start, column = 3)
        start = start + 1

    w.mainloop()
    
def select_all_ui3(result):
    global id_input, pw_input, name_input, tel_input
    w = Tk()
    w.geometry("700x900")
    w.title("나의 첫 윈도우")
    w.configure(bg="pink")
    
    id_text = Label(w, text="아이디 ", font=("궁서", 30), fg="blue", bg="pink")
    pw_text = Label(w, text="패스워드", font=("궁서", 30), fg="blue", bg="pink")
    name_text = Label(w, text="이름", font=("궁서", 30), fg="blue", bg="pink")
    tel_text = Label(w, text="전화번호", font=("궁서", 30), fg="blue", bg="pink")
    id_text.grid(row= 0, column = 0)
    pw_text.grid(row= 0, column = 1)
    name_text.grid(row= 0, column = 2)
    tel_text.grid(row= 0, column = 3)
    
    size = len(result)
    print(size)
    start = 1
    global count
    
    global id_result, pw_result, name_result, tel_result
    
    for record in result:
        if start == size:
            break
        id_result[count] = Button(w, text=record[0], font=("궁서", 30), fg="blue", bg="lime")
        pw_result = Label(w, text=record[1], font=("궁서", 30), fg="blue", bg="yellow")
        name_result = Label(w, text=record[2], font=("궁서", 30), fg="blue", bg="yellow")
        tel_result = Label(w, text=record[3], font=("궁서", 30), fg="blue", bg="yellow")
        id_result[count].grid(row= start, column = 0)
        pw_result.grid(row= start, column = 1)
        name_result.grid(row= start, column = 2)
        tel_result.grid(row= start, column = 3)
        start = start + 1
        count = count + 1

    w.mainloop()

def select_all_ui4(result):
    global id_input, pw_input, name_input, tel_input
    w = Tk()
    w.geometry("700x900")
    w.title("나의 첫 윈도우")
    w.configure(bg="pink")
   
    size = len(result)
    print(size)
    start = 1
    global count
    
    global id_result, pw_result, name_result, tel_result
    
    listbox = Listbox(w, selectmode='extended', height=0)
        
    for record in result:
        if start == size:
            break
        listbox.insert(count, record[0])
        listbox.insert(count, record[1])
        listbox.insert(count, record[2])
        listbox.insert(count, record[3])
        listbox.pack()

        start = start + 1
        count = count + 1

    w.mainloop()
def insert_ui():
    global id_input, pw_input, name_input, tel_input
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
    
    id_text.pack(side=RIGHT)
    id_input.pack()
    pw_text.pack()
    pw_input.pack()
    name_text.pack()
    name_input.pack()
    tel_text.pack()
    tel_input.pack()
    insert.pack()
    w.mainloop()
    
def select_result_ui(record):
    global id_input, pw_input, name_input, tel_input
    w = Tk()
    w.geometry("500x450")
    w.title("나의 첫 윈도우")
    w.configure(bg="green")
    
    id_text = Label(w, text="검색된 아이디", font=("궁서", 30), fg="blue", bg="pink")
    pw_text = Label(w, text="검색된 암호", font=("궁서", 30), fg="blue", bg="pink")
    name_text = Label(w, text="검색된 이름", font=("궁서", 30), fg="blue", bg="pink")
    tel_text = Label(w, text="검색된 전화번호", font=("궁서", 30), fg="blue", bg="pink")
    
    id_input = Label(w, text=record[0], font=("궁서", 30), fg="blue", bg="yellow")
    pw_input = Label(w, text=record[1], font=("궁서", 30), fg="blue", bg="yellow")
    name_input = Label(w, text=record[2], font=("궁서", 30), fg="blue", bg="yellow")
    tel_input = Label(w, text=record[3], font=("궁서", 30), fg="blue", bg="yellow")
    
    id_text.pack()
    id_input.pack()
    pw_text.pack()
    pw_input.pack()
    name_text.pack()
    name_input.pack()
    tel_text.pack()
    tel_input.pack()
    w.mainloop()