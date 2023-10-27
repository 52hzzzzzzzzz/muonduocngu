
# from tkinter import Tk, Frame, Checkbutton
# from tkinter import BooleanVar, BOTH

# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
  
#         self.parent = parent
#         self.initUI()
  
#     def initUI(self):
#         self.parent.title("Checkbutton")
#         self.pack(fill=BOTH, expand=True)
#         self.var = BooleanVar()
     
#         cb = Checkbutton(self, text="Show Title", variable=self.var, command=self.onClick)
#         cb.select()
#         cb.place(x=50, y=50)
  
#     def onClick(self):
#         if self.var.get() == True:
#             self.master.title("Checkbutton")
#         else:
#             self.master.title("")
  
# root = Tk()
# root.geometry("250x150+300+300")
# app = Example(root)
# root.mainloop()

# #-----------------------------------------------------------------------------------------------------------------------------------

# from PIL import Image, ImageTk
# from tkinter import Tk, Frame, Label

# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
  
#         self.parent = parent
  
#         self.initUI()
  
#     def initUI(self):
#         self.parent.title("Label")
  
#         self.img = Image.open("E:\\Courses\\Python\\rotunda.jpg")
#         rotunda = ImageTk.PhotoImage(self.img)
#         label = Label(self, image=rotunda)
  
#         label.image = rotunda
  
#         label.pack()
#         self.pack()
  
#     def setGeometry(self):
#         w, h = self.img.size
#         self.parent.geometry(("%dx%d+300+300") % (w, h))

# root = Tk()
# ex = Example(root)
# ex.setGeometry()
# root.mainloop()

# #-----------------------------------------------------------------------------------------------------------------------------------

# from tkinter import Tk, BOTH, IntVar, LEFT
# from tkinter.ttk import Frame, Label, Scale, Style

# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#         self.parent = parent
#         self.initUI()

#     def initUI(self):
#         self.parent.title("Scale")
#         self.style = Style()
#         self.style.theme_use("default")
  
#         self.pack(fill=BOTH, expand=1)
  
#         scale = Scale(self, from_=0, to=100, command=self.onScale)
#         scale.pack(side=LEFT, padx=15)
  
#         self.var = IntVar()
#         self.label = Label(self, text=0, textvariable=self.var)
#         self.label.pack(side=LEFT)

#     def onScale(self, val):
#         v = int(float(val))
#         self.var.set(v)

# root = Tk()
# ex = Example(root)
# root.geometry("250x100+300+300")
# root.mainloop()

# #-----------------------------------------------------------------------------------------------------------------------------------

from tkinter.ttk import Frame, Label
from tkinter import Tk, BOTH, Listbox, StringVar, END

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
  
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Listbox")
        self.pack(fill=BOTH, expand=1)
  
        acts = ["Scarlet Johansson", "Rachel Weiss", "Natalie Portman", "Jessica Alba"]
  
        lb = Listbox(self)
  
        for i in acts:
            lb.insert(END, i)
  
        lb.bind("<<ListboxSelect>>", self.onSelect)
  
        lb.pack(pady=15)
  
        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack()

    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)
  
        self.var.set(value)
  
root = Tk()
ex = Example(root)
root.geometry("300x250+300+300")
root.mainloop()
