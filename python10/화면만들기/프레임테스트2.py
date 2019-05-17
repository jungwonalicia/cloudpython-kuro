from tkinter import *
 
class MyApp: 
    def __init__(self,parent): 
        parent.geometry("300x200") 
        self.buttonframe=Frame(parent) 
        self.buttonframe.pack(side=LEFT) 
        self.button_side=StringVar() 
        for item in [TOP,BOTTOM,LEFT,RIGHT]: 
            Radiobutton(self.buttonframe, text=str(item), indicator=0, value=item, variable=self.button_side, command=self.update, width=10).pack() 
        self.testframe=Frame(parent,background="green") 
        self.testframe.pack(side=RIGHT,expand=YES,fill=BOTH) 
        self.labelX=Label(self.testframe,text="요구된 공간",background="yellow",width=10,height=1) 
        self.labelX.pack() 
        self.labelY=Label(self.testframe,text="요구되지 않은 공간",background="green") 
        self.labelY.pack(fill=BOTH,expand=YES) 
            
    def update(self): 
        self.labelX.pack(side=self.button_side.get(),fill=BOTH) 

root=Tk() 
myapp=MyApp(root) 
root.mainloop()

