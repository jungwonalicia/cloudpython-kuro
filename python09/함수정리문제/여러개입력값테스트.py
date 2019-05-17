def call(*parameter):
    print("전달받은 데이터 개수: " , len(parameter))

if __name__ == '__main__':
    call(1, 2, 3, 4, 5)
    call(1, 2, 3, 4)
    call(1, 2, 3)