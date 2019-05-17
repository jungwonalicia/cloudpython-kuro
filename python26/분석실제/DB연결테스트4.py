import pymysql
from tkinter import *

def db_select_all():
    con = pymysql.connect(host ='localhost', user = 'root', password = '1234', db = 'cloud')
    print("1. db인증-> 연결  성공....")
    print(con)
    
    '''2. 연결정보-> 통로'''
    cur= con.cursor()
    print("2. 연결정보-> 통로 만들기 성공....")
    
    '''3. sql문 만들어서 -> 전송'''
    sql = "select * from imgtable"
    print("생성된 sql:", sql)
    cur.execute(sql) 
    print("3. sql문 만들어서 -> 전송 성공....")
    result = []
#     con.commit()
    while True:
        record = cur.fetchone()
        if record == None:
            break
        else:
            print(record)
            result.append(record)
        
           
#     print(result)
    
    '''4. db 연결해제'''
    con.close()
    print("4. db 연결해제 성공....")
    return result
    
if __name__ == '__main__':
    result = db_select_all()
    print("내가 받아온 리스트: ", result)
    
    iconlist = []
    imglist = []    
    w = Tk()
    for i in range(0, len(result)):
        for j in range(0, len(result[i])):
            if j == 2:
                iconlist.append(PhotoImage(file=result[i][j]))
               
            else:
                i1 = Label(w, text=result[i][j])
                i1.pack()
    i2 = Label(w, image=iconlist[0])
    i3 = Label(w, image=iconlist[1])
    i2.pack()
    i3.pack()
    w.mainloop()
  
  
    
    



