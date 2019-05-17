import random

target = 10
# target = random.randrange(1, 101)
count = 0

while True:
    # print(count)
    count = count + 1
    
    data = int(input("숫자를 입력(1-100까지), 종료 0를 입력: " ))
    
    #종료 처리
    if data == 0:
        print("프로그램을 종료합니다.")
        break #반복문을 종료
    
    print("당신의 입력 숫자는 ", data)
    
    if target == data:
        print("정답입니다.")
        print("프로그램을 종료합니다.")
        print("당신이 시도한 횟수는: ", count)
        break
    else:
        print("정답이 아닙니다.")
        print("숫자를 다시 입력해주세요...")
        # 너무 커요!, 너무 작아요!
        if data > target:
            print("너무 커요!!!")
        else:
            print("너무 작아요!!!")
        print("--------------------")
    
    
    
    
    
    
    
    
    