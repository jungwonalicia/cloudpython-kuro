# 휴대폰 => class
# 정적특성- 색, 회사 => 멤버변수
# 동적특성- 인터넷검색하다, 사진을찍다 => 멤버함수
from numpy.core._dtype import __str__

class Phone:
    color = '';
    company = '';
    
    def search(self):
        print('인터넷 검색하다.')
        
    def picture(self):
        print('사진을 찍다.')

    def __str__(self):
        return self.color +" "+ self.company
        
p1 = Phone()
p1.color = '빨강'
p1.company = 'sk'

p2 = Phone()
p2.color = '파랑'
p2.company = 'abc'

p3 = Phone()
p3.color = '노랑'
p3.company = 'apple'

p1.picture()
p2.search()
p3.picture()

print(p1)
print(p2)
print(p3)



    
    
    
    
    
    