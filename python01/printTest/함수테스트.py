# 인원, 가격
# 입력을 받아서,

def inputFunc():
    person = int(input("인원 입력>> "))
    price = int(input("가격 입력>> "))
    return person * price

def process(x):
    if x >= 10000 :
        y = x- 2000
    else:
        y = x
    return y
    
# print("두 수를 곱한 값: " , inputFunc())
result = inputFunc()
print("두 수를 곱한 값: ", result)

total = process(result)
print("당신이 지불할 금액은 ", total)







# 두 수를 곱한 후,
# 곱한 수가 10000원이 넘으면, 2000원을 할인