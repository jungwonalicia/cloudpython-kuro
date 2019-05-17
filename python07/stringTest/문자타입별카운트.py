# 1) 문자열 입력
data = input("문자열 입력>> ")

#1. 리스트
count = [0, 0, 0] #0(숫자), 1(공백), 2(알파벳) 

#2. 각각 변수
alpha = 0
apace = 0
number = 0

#3. 딕셔너리
count2 = {"number":0, "space":0, "alpha":0}
 
# 2) for문을 이용해서 하나씩 꺼내옴.
# 3) if문을 이용해서 어떤 타입인지를 판별
for x in data:
    print(x)
    if x.isalpha():
        alpha = alpha + 1
    if x.isspace():
        apace = apace + 1
    if x.isdigit():
        number = number + 1
print()
print("alpha: ", alpha)
print("apace: ", apace)
print("digit: ", number)
       
# 4) 해당 타입을 카운트
#    누적시키기 위한 변수가 필요
#    (숫자, 공백, 알파벳)
# 5) 각 카운트 값 프린트