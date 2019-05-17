member = []

def insert(data):
    member.append(data)
    print(len(member))

for i in range(0, 3):
    data = input("이름 입력>> ")
    insert(data)

for i in range(0, len(member)):
    print(i, ":" , member[i])

print()

print(member)



    
