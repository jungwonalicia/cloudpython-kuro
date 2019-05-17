import os
import calendar

if __name__ == '__main__':
    cal = calendar.month(2019, 4)
    print(cal)
    print(os.getcwd())
    os.chdir("c:")
    print(os.getcwd())
    print(os.listdir("."))
    