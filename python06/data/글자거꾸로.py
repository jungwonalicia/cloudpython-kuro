data = "파이썬 프로그래머"
result = []

size = len(data)
print(size)
for x in range(size-1, -1, -1):
    print(x, ":" ,data[x])
    result.append(data[x])

print("결과 리스트 값: ", result)
for x in result:
    print(x, end=" ")    