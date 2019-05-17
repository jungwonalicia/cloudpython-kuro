def transfer(dog):
    print(dog.color)
    print(dog.field)
    
class Dog:
    #멤버 변수
    color = ''
    field = ''
    count = 0
    __test = 0
    test = 0

#     def __init__(self): # 오버로딩 안됨. 
#         print('나는 입력값 없어요.')
    
    def __init__(self, color, field):
        self.color = color
        self.field = field
#         Dog.count = Dog.count + 1
#         self.count= self.count + 1
#         self.__test = 1
        print(Dog.count)
#         print(self.count)
        
    #멤버 메소드
    def jump(self):
        print('뛰고 있다.')
        return self.__test

# 오버로딩 안됨.        
#     def jump(self, value):
#         print('뛰고 있다.')
    
    def sleep(self):
        print('자다')
        
    def __str__(self):
        return self.color + ", " + self.field

dog1 = Dog('갈색', '요크셔테리어')
print(dog1)
dog2 = Dog('흰색', '진돗개')
print(dog2)

print('---------------')

transfer(dog1) 

print(dog1.jump())
print(dog1.test) 
print(dog1.__test) #private변수 이므로, 클래스 외부 에서 접근 불가








    