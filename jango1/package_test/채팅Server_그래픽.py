from socket import *
from tkinter import *

sock = socket(AF_INET, SOCK_DGRAM)
sock2 = socket(AF_INET, SOCK_DGRAM)

def start():
    sock.bind(('192.168.0.10',6005))
    print('6005번 포트 소켓 시작됨..')


def send():    
    sock2.sendto('I am a server.'.encode('utf-8'), ('192.168.0.10', 5005))

if __name__ == '__main__':
    
    start()
    
    w = Tk()
    w.title('6005')
    b = Button(w, text="데이터 전송", command=send)
    b.pack()
    e = Entry(w)
    e.pack()
    t = Text()
    t.pack()
    w.mainloop()
    
    # while True:
    data, addr = sock.recvfrom(1024)
    print("나도 호출됨.")
    data2 = data.decode('utf-8')
    print('받은 데이터 : ', data2)
    t.insert(END, data2 + "\n")    