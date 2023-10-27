from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
var = StringVar()
var.set("one")
data=("one", "two", "three", "four")
cb = Combobox(window, values=data)
cb.place(x=60, y=150)



lb = Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END, num)
lb.place(x=250, y=250)

window.title("Hello Python")
window.geometry("400x300+10+10")
window.mainloop()