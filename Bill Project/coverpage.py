from tkinter import *
from tkinter import simpledialog
from PIL import Image, ImageTk
class Coverpage:
    def __init__(self,root):
        bg_color = "#074463"
        self.root=root
        self.root.geometry("800x300")
        self.root.resizable(False,False)
        self.root.eval('tk::PlaceWindow . center')

        image = Image.open("Coverpage.jpeg")
        resize_image = image.resize((800, 300))

        img = ImageTk.PhotoImage(resize_image)


        label1 = Label(image=img,text="Bill Management",fg="white",font=("playfair display",55,"bold"),compound=CENTER)
        label1.image = img
        label1.pack()
        def next():
            self.root.destroy()
            import login

        #label=Label(root,text="Bill Management",font=("times new roman",30,"italic"))
        #label.pack()
        b3=Button(self.root,text="Next",font=("times new roman", 13 ,"bold"),bg=bg_color,fg="white",padx=10,relief=GROOVE,command=next)
        b3.place(x=675,y=225)

root=Tk()
obj = Coverpage(root)
root.mainloop()