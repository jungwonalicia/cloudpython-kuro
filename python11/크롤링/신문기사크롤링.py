from tkinter import *
from urllib import request
from bs4 import BeautifulSoup

def saveFile():
    target = request.urlopen("http://www.chosun.com/site/data/rss/rss.xml")
    soup = BeautifulSoup(target, "html.parser")
    result = soup.select("item")
    print(type(result))
    print(len(result))
#     print(result)

    for item in result:
        title = item.select_one("title").string
        author = item.select_one("author").string
        pubDate = item.select_one("pubDate").string
        print(title, author, pubDate)
       
input       
def readFile():
    global input
    input = input("날씨 예보를 알고 싶은 도시명을 입력하세요.")
    readFile = open(input + ".txt", "r")
    contents = readFile.read()
    text.insert(END, contents)
    
    readFile.close()

w = Tk()
intro = Label(w, text="날씨 정보를 읽어오겠습니다.",
              fg = "blue",
              bg = "pink",
              font = "궁서 20 bold"
             )
intro.pack()

save = Button(w, text="웹사이트 크롤링 파일로 저장",
              fg = "blue",
              bg = "yellow",
              font = "궁서 20 bold",
              command = saveFile
             )
save.pack()
read = Button(w, text="날씨 정보 파일로부터 읽기",
              fg = "blue",
              bg = "yellow",
              font = "궁서 20 bold",
              command = readFile
             )
read.pack()

text = Text(w, height=7, width=20,
            fg = "white",
            bg = "green",
            font = "궁서 40 bold"
            )
text.pack()
              
              




w.mainloop()


