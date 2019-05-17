# 파이썬은 다중 상속 지원 됨.
class Object:
    name = '홍길동'

class Object1:
    age = 100

class Animal(Object, Object1):
    def food(self):
        print('먹다')

a1 = Animal()
print(a1.name)
print(a1.age)
