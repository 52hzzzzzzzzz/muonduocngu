# from PIL import Image, ImageTk
# from tkinter import Tk, Label, BOTH
# from tkinter.ttk import Frame, Style

# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)

#         self.parent = parent
#         self.initUI()
    
#     def initUI(self):
#         self.parent.title("Absolute positioning")
#         self.pack(fill=BOTH, expand=1)

#         Style().configure("TFrame", background="#333")

#         bard = Image.open("E:\\Courses\\Python\\bardejov.jpg")
#         bard=bard.resize((100,100),Image.ANTIALIAS)
#         bardejov = ImageTk.PhotoImage(bard)
#         label1 = Label(self, image=bardejov)
#         label1.image = bardejov
#         label1.place(x=20, y=20)

#         rot = Image.open("E:\\Courses\\Python\\rotunda.jpg")
#         rot=rot.resize((100,100),Image.ANTIALIAS)
#         rotunda = ImageTk.PhotoImage(rot)
#         label2 = Label(self, image=rotunda)
#         label2.image = rotunda
#         label2.place(x=40, y=160)

#         minc = Image.open("E:\\Courses\\Python\\mincol.jpg")
#         minc=minc.resize((100,100),Image.ANTIALIAS)
#         mincol = ImageTk.PhotoImage(minc)
#         label3 = Label(self, image=mincol)
#         label3.image = mincol
#         label3.place(x=170, y=50)

# root = Tk()
# root.geometry("300x280+300+300")
# app = Example(root)
# root.mainloop()

#------------------------------------------------------------------------------------------------------------------------------

# from tkinter import Tk, W, E
# from tkinter.ttk import Frame, Button, Style
# from tkinter.ttk import Entry

# class Example(Frame):

#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#         self.parent = parent
#         self.initUI()

#     def initUI(self):

#         self.parent.title("Calculator")

#         Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

#         self.columnconfigure(0, pad=3)
#         self.columnconfigure(1, pad=3)
#         self.columnconfigure(2, pad=3)
#         self.columnconfigure(3, pad=3)

#         self.rowconfigure(0, pad=3)
#         self.rowconfigure(1, pad=3)
#         self.rowconfigure(2, pad=3)
#         self.rowconfigure(3, pad=3)
#         self.rowconfigure(4, pad=3)
#         entry = Entry(self)
#         entry.grid(row=0, columnspan=4, sticky=W+E)
#         cls = Button(self, text="Cls")
#         cls.grid(row=1, column=0)
#         bck = Button(self, text="Back")
#         bck.grid(row=1, column=1)
#         lbl = Button(self)
#         lbl.grid(row=1, column=2)
#         clo = Button(self, text="Close")
#         clo.grid(row=1, column=3)
#         sev = Button(self, text="7")
#         sev.grid(row=2, column=0)
#         eig = Button(self, text="8")
#         eig.grid(row=2, column=1)
#         nin = Button(self, text="9")
#         nin.grid(row=2, column=2)
#         div = Button(self, text="/")
#         div.grid(row=2, column=3)

#         fou = Button(self, text="4")
#         fou.grid(row=3, column=0)
#         fiv = Button(self, text="5")
#         fiv.grid(row=3, column=1)
#         six = Button(self, text="6")
#         six.grid(row=3, column=2)
#         mul = Button(self, text="*")
#         mul.grid(row=3, column=3)

#         one = Button(self, text="1")
#         one.grid(row=4, column=0)
#         two = Button(self, text="2")
#         two.grid(row=4, column=1)
#         thr = Button(self, text="3")
#         thr.grid(row=4, column=2)
#         mns = Button(self, text="-")
#         mns.grid(row=4, column=3)

#         zer = Button(self, text="0")
#         zer.grid(row=5, column=0)
#         dot = Button(self, text=".")
#         dot.grid(row=5, column=1)
#         equ = Button(self, text="=")
#         equ.grid(row=5, column=2)
#         pls = Button(self, text="+")
#         pls.grid(row=5, column=3)

#         self.pack()
# root = Tk()
# app = Example(root)
# root.mainloop()

#------------------------------------------------------------------------------------------------------------------------------

# from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
# from tkinter.ttk import Frame, Label, Entry

# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)

#         self.parent = parent
#         self.initUI()

#     def initUI(self):
#         self.parent.title("Review")
#         self.pack(fill=BOTH, expand=True)

#         frame1 = Frame(self)
#         frame1.pack(fill=X)

#         lbl1 = Label(frame1, text="Title", width=6)
#         lbl1.pack(side=LEFT, padx=5, pady=5)

#         entry1 = Entry(frame1)
#         entry1.pack(fill=X, padx=5, expand=True)

#         frame2 = Frame(self)
#         frame2.pack(fill=X)

#         lbl2 = Label(frame2, text="Author", width=6)
#         lbl2.pack(side=LEFT, padx=5, pady=5)

#         entry2 = Entry(frame2)
#         entry2.pack(fill=X, padx=5, expand=True)

#         frame3 = Frame(self)
#         frame3.pack(fill=BOTH, expand=True)

#         lbl3 = Label(frame3, text="Review", width=6)
#         lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

#         txt = Text(frame3)
#         txt.pack(fill=BOTH, pady=5, padx=5, expand=True)

# root = Tk()
# root.geometry("300x300+300+300")
# app = Example(root)
# root.mainloop()

#------------------------------------------------------------------------------------------------------------------------------


from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Style
from tkinter.ttk import Entry

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent) 

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Calculator")

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        entry = Entry(self)
        entry.grid(row=0, columnspan=4, sticky=W+E)
        cls = Button(self, text="Cls")
        cls.grid(row=1, column=0)
        bck = Button(self, text="Back")
        bck.grid(row=1, column=1)
        lbl = Button(self)
        lbl.grid(row=1, column=2) 
        clo = Button(self, text="Close")
        clo.grid(row=1, column=3) 
        sev = Button(self, text="7")
        sev.grid(row=2, column=0) 
        eig = Button(self, text="8")
        eig.grid(row=2, column=1) 
        nin = Button(self, text="9")
        nin.grid(row=2, column=2) 
        div = Button(self, text="/")
        div.grid(row=2, column=3) 

        fou = Button(self, text="4")
        fou.grid(row=3, column=0) 
        fiv = Button(self, text="5")
        fiv.grid(row=3, column=1) 
        six = Button(self, text="6")
        six.grid(row=3, column=2) 
        mul = Button(self, text="*")
        mul.grid(row=3, column=3) 
      
        one = Button(self, text="1")
        one.grid(row=4, column=0) 
        two = Button(self, text="2")
        two.grid(row=4, column=1) 
        thr = Button(self, text="3")
        thr.grid(row=4, column=2) 
        mns = Button(self, text="-")
        mns.grid(row=4, column=3) 
       
        zer = Button(self, text="0")
        zer.grid(row=5, column=0) 
        dot = Button(self, text=".")
        dot.grid(row=5, column=1) 
        equ = Button(self, text="=")
        equ.grid(row=5, column=2) 
        pls = Button(self, text="+")
        pls.grid(row=5, column=3)
      
        self.pack()

root = Tk()
app = Example(root)
root.mainloop()
