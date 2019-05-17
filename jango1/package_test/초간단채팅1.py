import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("송신용 소켓이 생성되었음.")

sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(('192.168.0.10',3336))

while True:
    data = input("내가  입력>> ")
    sock.sendto(data.encode('utf-8'), ('192.168.0.10', 2225))
    
    data, addr = sock2.recvfrom(1024)
    print("네가 입력>> " , data.decode('utf-8'))



    