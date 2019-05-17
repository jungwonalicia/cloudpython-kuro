# 1) 문자열 입력
data = input("문자열 입력>> ")

count = [0, 0, 0] #0(숫자), 1(공백), 2(알파벳) 

# 2) for문을 이용해서 하나씩 꺼내옴.
# 3) if문을 이용해서 어떤 타입인지를 판별
alpha = 0
for x in data:
    print(x)
    if x.isalpha():
        count[2] = count[2] + 1
    if x.isspace():
        count[0] = count[0] + 1
    if x.isdigit():
        count[1] = count[1] + 1

print()
print("alpha: ", count[2])
print("space: ", count[0])
print("digit: ", count[1])
# 4) 해당 타입을 카운트
#    누적시키기 위한 변수가 필요
#    (숫자, 공백, 알파벳)
# 5) 각 카운트 값 프린트