from tkinter import *
from tkinter.ttk import Radiobutton   
import json
from types import SimpleNamespace

file = open("File.json")
fileJ=json.load(file)
data = '{"title": "Требовательность", "answers": {"text1": "1", "text2": "2", "text3": "3", "text4": "4", "text5": "5"}}'
fileObj = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
print(fileObj.title, fileObj.answers.text1, fileObj.answers.text2, fileObj.answers.text3, fileObj.answers.text4, fileObj.answers.text5)

def clicked():  
    lbl.configure(text=selected.get())

window = Tk()  
window.title("Главное окно")  
window.geometry('400x250')  
selected = IntVar()  

lbl = Label(window, text=fileObj.title)  
lbl.grid(column=0, row=0) 

rad1 = Radiobutton(window, text=fileObj.answers.text1, value=1, variable=selected)  
rad2 = Radiobutton(window, text=fileObj.answers.text2, value=2, variable=selected)  
rad3 = Radiobutton(window, text=fileObj.answers.text3, value=3, variable=selected)  
rad4 = Radiobutton(window, text=fileObj.answers.text4, value=4, variable=selected)  
rad5 = Radiobutton(window, text=fileObj.answers.text5, value=5, variable=selected)   
btn = Button(window, text="Кликни!", command=clicked)  

lbl = Label(window)  
rad1.grid(column=0, row=1)  
rad2.grid(column=0, row=2)  
rad3.grid(column=0, row=3)  
rad4.grid(column=0, row=4)
rad5.grid(column=0, row=5)  

btn.grid(column=7, row=0)  
lbl.grid(column=7, row=2) 

window.mainloop()

