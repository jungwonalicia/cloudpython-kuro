def call(**parameter):
    print("전달받은 데이터 개수: " , len(parameter))
    for x in parameter.keys():
        print(x , ": ", parameter[x], end=" ")
        print()
    
    
if __name__ == '__main__':
    call(감자 = 20, 고구마 = 40, 양파 = 60)