import random

data = ['a', 'b', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def passConstructor():
    for x in range(0, 6): #횟수 체크
        pw = random.choice(data)
        print(pw, end="")

if __name__ == '__main__':
    for x in range(0, 3): #횟수 체크
        passConstructor()
        print()
        
