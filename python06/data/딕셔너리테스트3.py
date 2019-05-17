data1 = { 1:"송아무개" , 2:"정아무개" , 3:"김아무개"}
print(data1)
print(data1[1])
print(data1[2])
print(data1[3])

print()
data2 = { "name":"송아무개" , "age":100 , "소속":"kg"}
print(data2)
print(data2["name"])
print(data2["age"])
print(data2["소속"])

print(data2.keys())
print(data2.values())
print(data2.items())

print()
data2["소속"] = "구로점"
print(data2)


# data2 = data1 #얕은 복사
# print(data2)
# 
# data3 = data1.copy() #깊은 복사
# print(data3)
# data1[1] = "박아무개"
# print(data2)
# print(data3)
