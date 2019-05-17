# 1) 문자열 입력
data = input("문자열 입력>> ")

#3. 딕셔너리
count2 = {"number":0, "space":0, "alpha":0}
 
# 2) for문을 이용해서 하나씩 꺼내옴.
# 3) if문을 이용해서 어떤 타입인지를 판별
for x in data:
    print(x)
    if x.isalpha():
        count2["alpha"] = count2["alpha"] + 1
    if x.isspace():
        count2["space"] = count2["space"] + 1
    if x.isdigit():
        count2["number"] = count2["number"] + 1
print()
print("alpha: ", count2["alpha"])
print("space: ", count2["space"])
print("digit: ", count2["number"])
       
# 4) 해당 타입을 카운트
#    누적시키기 위한 변수가 필요
#    (숫자, 공백, 알파벳)
# 5) 각 카운트 값 프린트