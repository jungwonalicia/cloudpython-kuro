singer = {1:"송아무개", 2:"김아무개", 3:"정아무개"}

print(singer.keys())
print()

for x in singer.keys():
    print("%s --> %s" % (x, singer[x]))
print()

print(singer.items())
print(singer)

print()

import operator
test1 = sorted(singer.items(), key=operator.itemgetter(1))
test2 = sorted(singer.items(), key=operator.itemgetter(0))
print(test1)
print(test2)




