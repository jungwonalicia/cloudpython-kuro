data = input("문자열을 입력하시오.")
print("입력받은 데이터: ", data)

data2 = data.split()
print(data2)

collect = []

print()
for x in data2:
#   print(x[0], end="")
    collect.append(x[0])

print(collect)
for y in collect:
    print(y, end="")
    
    