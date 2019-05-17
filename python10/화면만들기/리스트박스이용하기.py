from tkinter import *
from tkinter.messagebox import *


def go():
   index = listData.curselection()[0]
   print(index)
   print(listData.get(index))
   
    
w = Tk()

# 리스트박스선택값 = StringVar()

listData = Listbox(w, selectmode=SINGLE, bg="yellow")
listData.insert(0, "hi0")
listData.insert(1, "hi1")
listData.insert(2, "hi2")
listData.insert(3, "hi3")
listData.insert(4, "hi4")

listData.bind("<<ListboxSelect>>", lambda x : go())
    
listData.pack(side=LEFT)
w.mainloop()
    
    
    
    