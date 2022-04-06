from tkinter import *
import qrcode
import resizeimage.resizeimage
from PIL import Image,ImageTk
import mysql.connector
from resizeimage import *
from tkinter import messagebox

class Qr_Generator:

    def __init__(self, ui):
        bg_color = "#074463"
        self.root = ui
        self.root.geometry("900x500+200+50")
        self.root.title("Register Window")
        self.root.resizable(False, False)
        image = Image.open("register.jpeg")
        resize_image = image.resize((900, 500))

        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(image=img)
        label1.image = img
        label1.pack()
        Label(self.root, image=img).place(x=0, y=0, relwidth=1)

        #Employee frame
        self.var_ID = StringVar()
        self.var_Name = StringVar()
        self.var_Password = StringVar()

        emp_frame = Frame(self.root, bd=2, relief=RIDGE, bg=bg_color)
        emp_frame.place(x=50, y=100, width=400, height=350)

        Label(emp_frame, text="Employee Details", font=("Playfair Display", 20), fg='#8BDAFB', bg=bg_color).place(x=0,y=0,relwidth=1)
        Label(emp_frame, text="Employee ID", font=("Playfair Display", 15), fg='#8BDAFB', bg=bg_color).place(x=20,y=80)
        Label(emp_frame, text="Name", font=("Playfair Display", 15), fg='#8BDAFB', bg=bg_color).place(x=20,y=130)
        Label(emp_frame, text="Password", font=("Playfair Display", 15), fg='#8BDAFB', bg=bg_color).place(x=20,y=180)

        #Input Fields

        Entry(emp_frame, font=("Playfair Display", 15), textvariable=self.var_ID, fg='#8BDAFB', bg=bg_color,borderwidth=3, relief="solid").place(x=150,y=81)
        Entry(emp_frame, font=("Playfair Display", 15), textvariable=self.var_Name, fg='#8BDAFB', bg=bg_color,borderwidth=3, relief="solid").place(x=150, y=131)
        Entry(emp_frame, font=("Playfair Display", 15), textvariable=self.var_Password, fg='#8BDAFB', bg=bg_color,borderwidth=3, relief="solid").place(x=150, y=181)

        btn_generate = Button(emp_frame, text='Register', command=self.generate, font=("Playfair Display", 15)).place(x=50, y=240, width=100)
        btn_exit = Button(emp_frame, text='Exit', command=self.exitt, font=("Playfair Display", 15)).place(x=225, y=240, width=100)
        self.msg=''
        self.lbl_msg=Label(emp_frame, text=self.msg, font=("Playfair Display", 15), fg='black', bg=bg_color)
        self.lbl_msg.place(x=0, y=300, relwidth=1)

        #QR frame
        qr_frame = Frame(self.root, bd=2, relief=RIDGE, bg=bg_color)
        qr_frame.place(x=500, y=100, width=350, height=230)

        Label(qr_frame, text="Your QR", font=("Playfair Display", 20), fg='#8BDAFB', bg=bg_color).place(x=0,y=0,relwidth=1)
        self.qr_code = Label(qr_frame,text='Your QR',font=("Playfair Display", 20))
        self.qr_code.place(x=100,y=50,width=150,height=150)
    def exitt(self):
        self.root.destroy()
        import login
    def generate(self):

        if self.var_ID.get()=='' or self.var_Name.get()=='' or self.var_Password.get()=='':
            messagebox.showerror(title="error", message="All fields are required")
        else:
            qr_data= (f"{self.var_ID.get()}")
            qr_code= qrcode.make(qr_data)
            print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[150,150])
            qr_code.save("Employee_QR/"+str(self.var_ID.get()+'.png'))

            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            messagebox.showinfo(title="register", message="Registered succesfully")

            def insert():
                userid=self.var_ID.get()
                name = self.var_Name.get()
                password = self.var_Password.get()

                con = mysql.connector.connect(host="localhost", user="root", password="nikunj22", database="bill_system")
                cursor = con.cursor(buffered= True)
                cursor.execute("show tables")
                cursor.execute("insert into register values('" + userid + "','" + name +"','" + password + "')")
                cursor.execute("commit");
                con.close();
            insert()

root = Tk()
obj = Qr_Generator(root)
root.mainloop()

