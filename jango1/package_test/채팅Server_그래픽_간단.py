from socket import *
from tkinter import *

def send():    
    connectionSock.send('I am a server.'.encode('utf-8'))
    print('메시지를 보냈습니다.')

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('127.0.0.1', 5566))
print("TCP서버가 시작되었습니다.")
serverSock.listen(1)
print("클라이언트 요청을 기다리는 중.....")

w = Tk()
b = Button(w, text="데이터 전송", command=send)
b.pack()
e = Entry(w)
e.pack()
t = Text()
t.pack()
w.mainloop()

while True:
    connectionSock, addr = serverSock.accept()
    
    print(str(addr),'에서 접속이 확인되었습니다.')
    
    data = connectionSock.recv(1024)
    data2 = data.decode('utf-8')
    print('받은 데이터 : ', data2)
    t.insert(END, data2 + "\n")
    


