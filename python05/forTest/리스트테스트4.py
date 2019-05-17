data_list = []
for x in range(0, 10): 
    data = int(input("숫자입력: >> "))
    data_list.append(data)

# data_list = [2, 4, 5, 5, 3, 1, 2, 3, 4, 3]
sum = 0
for i in range(0, 10):
    sum = sum + data_list[i]

print(sum)








