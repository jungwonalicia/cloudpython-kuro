data = "파이썬은 아주 Easy!!! but High..."

print(data.upper())
print(data.lower())
print(data.swapcase())
print(data.title())

print()
data = "파이썬은 아주 Easy!!! but High..."
print(len(data))
print(data.count(' '))
print(data.find('아주'))
print(data.startswith("파"))
print(data.endswith("."))

print()
data = "  파이썬은  아주  Easy!!!  but  High...  "
print(data.strip()) 
print(data.rstrip())
print(data.lstrip()) 

data2 = data.replace("아주", "장고")
print(data2)

print()
data = "파이썬은  아주  Easy!!!  but  High..."
print(data.split("!!!"))
data2 = "정말인가요??"
print(data + data2)
print(data)
data3 = data + data2
print(data3)
print(data.join(data2))
print(data)














