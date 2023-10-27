from tkinter import *
window=Tk()
# add widgets here

btn = Button(window, text="This is Button widget", fg='white', bg="black", font=("Helvetica", 16))
btn.place(x=80, y=100)

window.title('Hello Python')
window.geometry("500x500+10+20")
window.mainloop()