import operator

trainList = {"토마스":5, "헨리":8, "에드워드":9, "에밀리":5,
             "퍼시":5, "고든":13
             }
print("기차 수송량 목록: ", trainList)

trainList2 = sorted(trainList.items(), key=operator.itemgetter(1), reverse=True)
print(type(trainList2))
print(trainList2)

trainList3 = dict(trainList2)

print("---------------------------")
print("기차\t 수송량\t 순위")
print("---------------------------")
keys = list(trainList3.keys())
values = list(trainList3.values())

for x in range(0, 6):
    print(keys[x], end="\t")
    print(values[x], end="\t")
    print(x + 1)

