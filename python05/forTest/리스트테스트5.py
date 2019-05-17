eng = []
math = []

for x in range(0, 3):
    e = int(input("영어 >>"))
    eng.append(e)
    m = int(input("수학 >>"))
    math.append(m)

print(eng)
print(math)

engSum = 0
mathSum = 0

for x in range(0, 3):
    engSum = engSum + eng[x]
    mathSum = mathSum + math[x]

print(engSum/len(eng))
print(mathSum/len(math))






 
    

