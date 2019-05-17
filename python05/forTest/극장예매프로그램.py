seat2 = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0," "," "," "," ", 0, 0],
         [0, 0, 0, " ", " ", 0, 0, 0]]

while True:
    print("   ", end="")
    for i in range(0, 8):
        print(" ", i,  end="")
    print("\n---------------------------")
    for x in range(0, len(seat2)): #행을 출력해주는 반복문
        print(x , "행: ", end="")
        for y in range(0, len(seat2[x])): #열을 출력해주는 반복문
            print(seat2[x][y], end="  ")
        print()
    print("---------------------------")
    
    select = input("예매 1, 종료0번을 입력하세요.")
    if select == "0":
        print("예매 프로그램을 종료합니다.")
        break
    else:
        data1 = int(input("앉고 싶은 좌석을 입력하세요.(행)"))
        data2 = int(input("앉고 싶은 좌석을 입력하세요.(열)"))
        if seat2[data1][data2] == 1:
            print("이미 예매가 완료된 자리입니다.")
            print("다시 좌석을 선택해주세요.")
        else:    
            seat2[data1][data2] = 1
            print("예매가 완료되었습니다.")
    










