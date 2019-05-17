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
print("기차\t 수송량\t ")
print("---------------------------")
keys = list(trainList.keys())
values = list(trainList.values())
# print(len(keys))
# print(len(values))
y = 0
for x in trainList.keys():
    print(keys[y], end="\t")
    print(values[y], end="\t")
    print()
    y = y + 1

