from tkinter import Tk, Label, PhotoImage
    
if __name__ == "__main__":
    root = Tk()
    root.title("글씨와 그림이 어울리도록 compound 속성을 설정하는 방법")
      
    imgObj = PhotoImage(file = "web.png")
       
    compLabel = Label(root)
    compLabel["image"] = imgObj
    compLabel["text"] = "이것은 글씨"
    compLabel["compound"] = "top"
    compLabel.pack()
        
    root.mainloop()