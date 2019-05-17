'''
변수의 생존 범위에 따라 분류: 전역변수, 지역변수
'''
colors = []
def dataInput():
    for x in range(0, 5):
        data = input("색깔을 입력>> ")
        colors.append(data)

def dataPrint():
    print("내가 좋아하는 색깔은: ", end=" ")
    for x in colors:
        print(x, end=" ")

if __name__ == '__main__':
    dataInput()
    dataPrint()