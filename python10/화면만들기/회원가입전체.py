from 화면만들기.나의윈도우3 import *
from db.DB연결테스트4 import db_select_all
from tkinter import *


if __name__ == '__main__':
    w = Tk()
    w.geometry("500x450")
    w.title("나의 첫 윈도우")
    
    insert = Button(w, 
                    text="회원가입 처리", 
                    font=("궁서", 30), 
                    fg="red", 
                    bg="yellow", 
                    command=insert_ui)
    insert.pack()
    
    delete = Button(w, 
                    text="회원탈퇴 처리", 
                    font=("궁서", 30), 
                    fg="red", 
                    bg="yellow", 
                    command=delete_ui)
    delete.pack()
    
    update = Button(w, 
                    text="회원수정 처리", 
                    font=("궁서", 30), 
                    fg="red", 
                    bg="yellow", 
                    command=update_ui)
    update.pack()
    
    select = Button(w, 
                    text="회원검색 처리", 
                    font=("궁서", 30), 
                    fg="red", 
                    bg="yellow", 
                    command=select_ui)
    select.pack()
    
    select_all = Button(w, 
                    text="회원목록 처리", 
                    font=("궁서", 30), 
                    fg="red", 
                    bg="yellow", 
                    command=select_all_process3)
    select_all.pack()
    
    w.mainloop()
    
    