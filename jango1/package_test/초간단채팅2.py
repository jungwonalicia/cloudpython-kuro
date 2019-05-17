import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock2.bind(('192.168.0.10',2225))
print("수신용 소켓이 생성되었음.")

while True:
    data, addr = sock2.recvfrom(1024)
    print("네가 입력>> " , data.decode())
    
    data2 = input("내가 입력>> ")
    sock.sendto(data2.encode(), (('192.168.0.10',3336)))