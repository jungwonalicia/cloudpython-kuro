from tkinter import *

w = Tk()
colors = ["green", "red", "orange", "white", "yellow", "blue"]
print(len(colors), "개의 리스트 항목이 들어있음.")
print(colors[0])

r = 0 #행번호(가로줄)

for c in colors:
    print(c) #green~~~
    l = Label(w, 
            text = c,
            width = 15
    )
    l.grid(row = r, column = 0)

    b = Button(w,
            bg = c, 
            width = 15
    )
    b.grid(row = r, column = 1)
    r = r + 1;

w.mainloop()