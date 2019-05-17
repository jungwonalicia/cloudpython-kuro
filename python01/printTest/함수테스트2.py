# 1. 입력받는 함수 정의
#     좋아하는 색은(빨강:1, 노랑:2, 파랑:3)
# 2. 입력받은 값을 반환받아,
#     1이면, 파이썬 스터디반.
#     2이면, 장고 스터디반.
#     3이면, 웹구축 스터디반.
#     if, if~else, if~elif~~~else
def inputFunc():
    color = input("좋아하는 색은: ")
    return color

def classFunc(color):
    if color == "1":
        finalResult = "파이썬 스터디반"
    elif color == "2":
        finalResult = "장고 스터디반"
    else:
        finalResult = "웹구축 스터디반"
    return finalResult

color = inputFunc()
print(classFunc(color))






