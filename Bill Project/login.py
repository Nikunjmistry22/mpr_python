from tkinter import *
from PIL import Image,ImageTk
class Login:
    def __init__(self,root):
        bg_color="#074463"
        self.root=root
        self.root.geometry("400x400")
        self.root.resizable(False,False)
        self.root.eval('tk::PlaceWindow . center')
        image = Image.open("login.jpeg")
        resize_image = image.resize((400, 400))

        img = ImageTk.PhotoImage(resize_image)

        label1 = Label(image=img)
        label1.image = img
        label1.pack()
        def login():
            self.root.destroy()
            import qrreader

        def Register():
            self.root.destroy()
            import register

        b1=Button(self.root,text="Login",font=("times new roman", 13, "bold"),padx=10,relief=GROOVE,command=login,fg="white",background=bg_color)
        b1.place(x=170,y=120)

        b2=Button(self.root,text="Register",font=("times new roman", 13, "bold"),padx=10,relief=GROOVE,command=Register,fg="white",background=bg_color)
        b2.place(x=160,y=170)

        b3=Button(self.root,text="Exit",font=("times new roman", 13 ,"bold"),padx=10,relief=GROOVE,command=exit,fg="white",background=bg_color)
        b3.place(x=175,y=220)


root=Tk()
obj = Login(root)
root.mainloop()