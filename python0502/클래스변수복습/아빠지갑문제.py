class Girl:
    name = ''
    age = 0
    money = 10000
    
    def __init__(self, name, age):
        self.name = name #인스턴스 변수
        self.age = age #인스턴스 변수
        Girl.money = Girl.money - 1000 #클래스 변수
    
    def play(self):
        return '매일 놀아요.'
    
    def tv(self):
        print('tv를 봐요.')

    def __repr__(self):
        return self.name + " " + str(self.age)
    
girl1 = Girl('김연아', 15)
print(Girl.money)
girl2 = Girl('김세리', 10)
print(Girl.money)

print(girl1.name," ,", girl2.name)
    
print(girl1)
print(girl2)

print(girl1.play())
girl1.tv()
    
    
    
    
    