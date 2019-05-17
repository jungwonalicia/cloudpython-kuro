seat = [[1, 2, 3],[4, 5, 6]]

print(len(seat) , end=" ")  #행 수.

print(len(seat[0]) , end=" ")
print(len(seat[1]) , end=" ")

print("\n-----------------")

seat2 = [[1, 2, 3, 4],[5, 6],[7, 8, 9]]
for i in range(0, 3):
    print(len(seat2[i]) , end=" ")
# print(len(seat2[0]) , end=" ")
# print(len(seat2[1]) , end=" ")
# print(len(seat2[2]) , end=" ")
print("\n-----------------")
seat2 = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0," "," "," "," ", 0, 0],
         [0, 0, 0, " ", " ", 0, 0, 0]]
print("\n-----------------")

for x in range(0, len(seat2)): #행을 출력해주는 반복문
    for y in range(0, len(seat2[x])): #열을 출력해주는 반복문
        print(seat2[x][y], end=" ")
    print()
    
















