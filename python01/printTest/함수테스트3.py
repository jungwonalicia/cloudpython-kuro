def money1000(money):
#   나머지 연산자: //, / 
    c1000 = money // 1000
    print("1000원짜짜리 " , c1000, "장")
    return money % 1000

money = money1000(5500)
print("나머지 : ", money) 
