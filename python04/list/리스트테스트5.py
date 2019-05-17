list = [1, 5, 8, 2, 3, 9, 7]
print(list)

list.append(4);
print(list)

print(list.pop())
print(list)

print(list.sort())
print(list)

print("---------------------")
list2 = [1, 5, 8, 2, 3, 9, 7]
list3 = sorted(list2)
print(list2)
print(list3)

# list2.reverse() #역순 정렬
# print(list2)
min = list3[0]
max_index = len(list3) - 1
max = list3[max_index]
print("최소값: ", min)
print("최대값: ", max)

print("최소값의 위치: " , list2.index(min))
print("최대값의 위치: " , list2.index(max))

list2.insert(0, 4)
print(list2)

print(list2.count(4))
list3.clear()
print(list3)

print(list2.remove(4))
print(list2)

print(len(list2))

print("--------------------------")
list4 = [1, 2, 3]
list5 = [4, 5, 6]

print(list4.extend([7, 8, 9]))
print(list4)
print(list4.extend(list5))
print(list4)


list6 = []
list6 = list4
print(list4)
print(list6)
print("------<< 얕은 복사 >>------------")
list4[0] = 0
print(list4)
print(list6) 
print("------<< 깊은 복사 >>------------")
list7 = []
list7 = list4.copy()
print(list7)
list4[0] = 1
print(list4)
print(list7) 












































