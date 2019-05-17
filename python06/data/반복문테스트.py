data1 = ["감자", "고구마", "양파"]

for x in range(0, 3):
    print(data1[x])

for y in data1:
    print(y)

print()

data2 = "나는 파이썬 프로그래머"
for z in data2:
    print(z)
print()

singer = {1:"송아무개", 2:"김아무개", 3:"정아무개"}
data3 = singer.keys()
print(data3)

for j in data3:
    print(singer[j])

print()
for j in singer.keys():
    print(singer[j])
    print(singer.get(j))

print(1 in singer)
print("나" in data2)
print("감자" in data1)

    




