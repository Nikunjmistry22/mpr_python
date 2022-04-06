from tkinter import *
from tkinter import simpledialog,messagebox
import connection
class Password:
    def __init__(self,root):
        bg_color="#074463"
        self.root=root
        self.root.geometry("500x150")
        self.root.resizable(False,False)
        self.root.configure(bg="white")
        self.root.eval('tk::PlaceWindow . center')
        def get_password():
            s1=simpledialog.askstring("input string","Enter your password")
            b=connection.password()
            for i in b:
                if s1==i:
                    self.root.destroy()
                    import main
                else:
                    messagebox.showerror('Error','Invalid Password')
        b1=Button(self.root,text="password",font=("times new roman", 13, "bold"),padx=10,relief=GROOVE,fg="white",background=bg_color,command=get_password)
        b1.place(x=200,y=25)

        b3=Button(self.root,text="Exit",font=("times new roman", 13 ,"bold"),padx=10,relief=GROOVE,command=exit,fg="white",background=bg_color)
        b3.place(x=220,y=75)

root=Tk()
obj = Password(root)
root.mainloop()