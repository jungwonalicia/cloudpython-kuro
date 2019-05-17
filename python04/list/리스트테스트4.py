list = [1, 5, 8, 2, 3, 9, 7]

print(list)
print(list.pop()) #7을 프린트, 마지막값 뺌.
print(list) #7빼고 프린트
print(list.sort()) #파괴 함수(오름차순)
print(list) #정렬된 상태의 list
print(list.reverse()) #파괴 함수(내림차순)
print(list) #정렬된 상태의 list
print(list.index(8)) #8이 들어있는 위치값 리턴
print(list) #정렬된 상태의 list
list.remove(1) #값 1을 삭제
print(list) #정렬된 상태의 list
list.extend([6, 1, 4])
print(list) #추가된 상태의 list

list2 = [10, 12, 11]
list.extend(list2)
print(list)

list3 = sorted(list2) #비파괴 함수
print(list2)
print(list3)


