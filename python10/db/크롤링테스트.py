from tkinter import *
from urllib import request
from bs4 import BeautifulSoup

def saveFile():
    target = request.urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
    soup = BeautifulSoup(target, "html.parser")
    for location in soup.select("location"):
        city = location.select_one("city").string
        wf = location.select_one("wf").string
        tmn = location.select_one("tmn").string
        tmx = location.select_one("tmx").string
        
        saveFile = open(city + "2.txt", "w")
        saveFile.write(city + "\n")
        saveFile.write(wf + "\n")
        saveFile.write(tmn + "\n")
        saveFile.write(tmx + "\n")

def readFile():
    global input
    input = input("읽어올 파일명을 입력하세요.")
    readFile = open(input, "r")
    contents = readFile.read() #파일 전체 내용 읽기 
    text.insert(END, contents)


w = Tk()
#라벨 1개
intro = Label(w, text = "오늘 배운 내용 정리 윈도우 입니다.",
            fg = "red",
            bg = "yellow",
            font = "굴림 25 bold"
)
#버튼 2개
#웹사이트 클로링 파일로 저장
save = Button(w, text = "웹사이트 클로링 파일로 저장",
            fg = "blue",
            bg = "pink", 
            font = "궁서 20 bold",
            command = saveFile
)
#파일에서 읽기
read = Button(w, text = "파일에서 읽기",
            fg = "blue",
            bg = "pink", 
            font = "궁서 20 bold",
            command = readFile
)

text = Text(w, height = 10, width =  40, 
            bg = "green", 
            fg = "white",
            font = "바탕체 15 bold"
)
text.insert(END, "여기가 파일 읽어서 넣을 자리입니다.\n-----------------------\n")

intro.pack()
save.pack()
read.pack()
text.pack()

w.mainloop()