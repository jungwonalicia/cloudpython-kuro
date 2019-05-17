'''전역변수'''
x = 300

def call2():
    print("전역변수 접근: ", x)
    
def call():
    '''지역변수'''
    x = 20
    print("함수 내의 x변수값(지역변수):", x)

    y = 30
    print("함수 내의 y변수값(지역변수):", y)

if __name__ == '__main__':
    print("함수 밖의 x변수값(전역변수): ", x)
#     print(y) 지역변수 접근 불가
    call2()
    call()
    
    
    
    
    
