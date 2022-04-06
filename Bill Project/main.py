from tkinter import *
import datetime,flask
import pywhatkit as kit
from tkinter import simpledialog,messagebox
import random,math,os,connection,mysql.connector
from ttkwidgets.autocomplete import AutocompleteEntry
class BillApp:
    def __init__(self, root):
        bg_color="#074463"
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title('Billing Software')
        self.root.resizable(False, False)
        #self.root.eval('tk::PlaceWindow . center')
        title = Label(self.root, text="Billing Software", font=("times new roman", 30, "bold"), pady=2,fg="white",background=bg_color).pack()

        # =========Customer detail Frame=========
        F1 = LabelFrame(self.root, text="Customer Details", font=("times new roman", 15, "bold"),fg="white",background=bg_color)
        F1.place(x=0, y=80, relwidth=1)
        #Variables==============
        self.apple=IntVar()
        self.banana=IntVar()
        self.berries=IntVar()
        self.yogurd=IntVar()
        self.milk=IntVar()
        self.oil=IntVar()
        self.avocado=IntVar()
        self.salmon=IntVar()
        self.eggs=IntVar()
        self.chicken=IntVar()
        self.chickpeas=IntVar()
        self.lettuce=IntVar()
        self.zucchini=IntVar()
        self.cucumber=IntVar()
        self.brocoli=IntVar()
        self.carrot=IntVar()
        self.rice=IntVar()
        self.Qatmeal=IntVar()

        #Tax details and Total price===============
        self.grocery_tax=StringVar()
        self.total_grocery_price=StringVar()

        #Customer Details===========
        self.c_name=StringVar()
        self.c_no=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()



        def total():
            self.grocery_price= float(
                self.apple.get()*100+
                self.banana.get()*100+
                self.berries.get()*100+
                self.yogurd.get()*100+
                self.milk.get()*100+
                self.oil.get()*100+
                self.avocado.get()*100+
                self.salmon.get()*100+
                self.eggs.get()*100+
                self.chicken.get()*100+
                self.chickpeas.get()*100+
                self.lettuce.get()*100+
                self.zucchini.get()*100+
                self.cucumber.get()*100+
                self.brocoli.get()*100+
                self.carrot.get()*100+
                self.rice.get()*100+
                self.Qatmeal.get()*100
            )
            self.total_grocery_price.set("Rs. "+str(self.grocery_price))
            self.grocery_tax.set("Rs. "+str(self.grocery_price*0.05))
        def clear():
            self.apple.set(0)
            self.banana.set(0)
            self.berries.set(0)
            self.yogurd.set(0)
            self.milk.set(0)
            self.oil.set(0)
            self.avocado.set(0)
            self.eggs.set(0)
            self.salmon.set(0)
            self.chicken.set(0)
            self.chickpeas.set(0)
            self.lettuce.set(0)
            self.zucchini.set(0)
            self.cucumber.set(0)
            self.brocoli.set(0)
            self.carrot.set(0)
            self.rice.set(0)
            self.Qatmeal.set(0)
            self.c_name.set("")
            self.c_no.set("")
            self.search_bill.set("")
            self.grocery_tax.set("")
            self.total_grocery_price.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            welcome_bill()
        def welcome_bill():
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"    Welcome Grocecam Retail\n")
            self.txtarea.insert(END,f"\n Bill No: {self.bill_no.get()}")
            self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
            self.txtarea.insert(END,f"\n Phone Number: {self.c_no.get()}")
            self.txtarea.insert(END,f"\n ============================")
            self.txtarea.insert(END,f"\n Products\t    OTY\t    Price")
            self.txtarea.insert(END,f"\n ============================")

        def bill_area():
            if self.c_name.get()== "" or self.c_no.get() =="":
                messagebox.showwarning('Error','All fields are requiered')
            else:
                welcome_bill()
                if self.apple.get()!=0:
                    self.txtarea.insert(END,f"\n Apple\t       {self.apple.get()}\t      {self.apple.get()*100}")
                if self.banana.get()!=0:
                    self.txtarea.insert(END,f"\n Banana\t       {self.banana.get()}\t      {self.banana.get()*100}")
                if self.berries.get()!=0:
                    self.txtarea.insert(END,f"\n Berries\t       {self.berries.get()}\t      {self.berries.get()*100}")
                if self.milk.get()!=0:
                    self.txtarea.insert(END,f"\n Milk\t       {self.milk.get()}\t      {self.milk.get()*100}")
                if self.oil.get()!=0:
                    self.txtarea.insert(END,f"\n Olive Oil\t       {self.oil.get()}\t      {self.oil.get()*100}")
                if self.avocado.get()!=0:
                    self.txtarea.insert(END,f"\n Avacado\t       {self.avocado.get()}\t      {self.avocado.get()*100}")
                if self.salmon.get()!=0:
                    self.txtarea.insert(END,f"\n Salmon\t       {self.salmon.get()}\t      {self.salmon.get()*100}")
                if self.eggs.get()!=0:
                    self.txtarea.insert(END,f"\n Eggs\t       {self.eggs.get()}\t      {self.eggs.get()*100}")
                if self.chicken.get()!=0:
                    self.txtarea.insert(END,f"\n Chicken\t       {self.chicken.get()}\t      {self.chicken.get()*100}")
                if self.chickpeas.get()!=0:
                    self.txtarea.insert(END,f"\n Chickpeas\t       {self.chickpeas.get()}\t      {self.chickpeas.get()*100}")
                if self.lettuce.get()!=0:
                    self.txtarea.insert(END,f"\n Lettuce\t       {self.lettuce.get()}\t      {self.lettuce.get()*100}")
                if self.zucchini.get()!=0:
                    self.txtarea.insert(END,f"\n Zucchini\t       {self.zucchini.get()}\t      {self.zucchini.get()*100}")
                if self.cucumber.get()!=0:
                    self.txtarea.insert(END,f"\n Cucumber\t       {self.cucumber.get()}\t      {self.cucumber.get()*100}")
                if self.brocoli.get()!=0:
                    self.txtarea.insert(END,f"\n Brocoli\t       {self.brocoli.get()}\t      {self.brocoli.get()*100}")
                if self.carrot.get()!=0:
                    self.txtarea.insert(END,f"\n Carrots\t       {self.carrot.get()}\t      {self.carrot.get()*100}")
                if self.rice.get()!=0:
                    self.txtarea.insert(END,f"\n Brown Rice\t       {self.rice.get()}\t      {self.rice.get()*100}")
                if self.Qatmeal.get()!=0:
                    self.txtarea.insert(END,f"\n Qatmeal\t       {self.Qatmeal.get()}\t      {self.Qatmeal.get()*100}")

                self.txtarea.insert(END,f"\n ----------------------------")
                if self.grocery_tax.get()!="Rs. 0.0":
                    self.txtarea.insert(END,f"\n Grocery Tax\t\t   {self.grocery_tax.get()}")
                self.txtarea.insert(END,f"\n Total Bill\t\t   Rs: {float(self.grocery_tax.get()[4::])+float(self.total_grocery_price.get()[4::])}")
                self.txtarea.insert(END,f"\n ----------------------------")

                def insert():
                    s = self.txtarea.get("3.0", "4.0")
                    bill = s[-5:-1]
                    con = mysql.connector.connect(host="localhost", user="root", password="nikunj22",
                                                  database="bill_system")
                    cursor = con.cursor(buffered=True)
                    cursor.execute("show tables")
                    cursor.execute("insert into bill values('" + self.c_name.get() + "','" + self.c_no.get() + "','" + bill+ "')")
                    cursor.execute("commit");
                    con.close();



                def save_bill():
                    op=messagebox.askyesno("Save bill","Do you want to save the bill?")
                    if op>0:
                        self.bill_data=self.txtarea.get('1.0',END)
                        f1=open("bills/"+str(self.bill_no.get())+".txt","w")
                        f1.write(self.bill_data)
                        f1.close()
                        insert()

                        #self.txtarea.save("bills/"+str(self.txtarea.get('1.0',END)+'.txt'))
                        messagebox.showinfo(message="Bill is saved succesfully")
                    else:
                        return
                save_bill()
        def find_bill():
            present="no"
            for i in os.listdir("bills/"):
                if i.split('.')[0]==self.search_bill.get():
                    f1=open(f"bills/{i}","r")
                    self.txtarea.delete("1.0",END)
                    for d in f1:
                        self.txtarea.insert(END,d)
                    f1.close()
                    present="yes"
            if present=="no":
                    messagebox.showerror('Error','Invalid Bill No')

        def message():
            def addSecs(tm, secs):
                fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
                fulldate = fulldate + datetime.timedelta(seconds=secs)
                return fulldate.time()

            a = datetime.datetime.now().time()
            b = addSecs(a, 70)
            generatorotp = str(random.randint(000000, 100000))
            kit.sendwhatmsg('+91' + phone_txt.get(), 'otp:' + generatorotp, b.hour, b.minute)

            class Otp:
                def __init__(self, root1):
                    self.root1 = root1
                    self.root1.geometry("500x150")
                    self.root1.resizable(False, False)
                    self.root1.eval('tk::PlaceWindow . center')
                    self.txtarea=ta()

                    def otp():
                        s1 = simpledialog.askstring("input string", "Enter your OTP")
                        if s1 == generatorotp:
                            def addSecs(tm, secs):
                                fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
                                fulldate = fulldate + datetime.timedelta(seconds=secs)
                                return fulldate.time()

                            a = datetime.datetime.now().time()
                            b = addSecs(a, 90)
                            kit.sendwhatmsg('+91' + phone_txt.get(), self.txtarea, b.hour, b.minute)
                        else:
                            messagebox.showerror(message="Invalid OTP")

                    b1 = Button(self.root1, text="OTP", font=("times new roman", 13, "bold"), padx=10, relief=GROOVE,
                                command=otp)
                    b1.place(x=218, y=25)
                    b3 = Button(self.root1, text="Exit", font=("times new roman", 13, "bold"), padx=10, relief=GROOVE,
                                command=exit)
                    b3.place(x=220, y=75)
            root=Tk()
            obj=Otp(root)
            root.mainloop()
        cname_lb1 = Label(F1, text="Customer name", font=("times new roman", 18, "bold"),fg="white",background=bg_color).grid(row=0, column=0, padx=20,
                                                                                               pady=5)
        cname_txt = AutocompleteEntry(F1, width=15, textvariable=self.c_name,font="arial 15",background=bg_color,completevalues=connection.name()).grid(row=0, column=1, padx=10, pady=5)

        cname_lb2 = Label(F1, text="Phone number", font=("times new roman", 18, "bold"),fg="white",background=bg_color).grid(row=0, column=2, padx=20,
                                                                                              pady=5)
        phone_txt = Entry(F1, width=15, textvariable=self.c_no,font="arial 15",fg="white",background=bg_color)
        phone_txt.grid(row=0, column=3, padx=10, pady=5)

        cbill_no = Label(F1, text="Bill No", font=("times new roman", 18, "bold"),fg="white",background=bg_color).grid(row=0, column=4, padx=20,
                                                                                        pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.search_bill,font="arial 15",fg="white",background=bg_color).grid(row=0, column=5, padx=10, pady=5)

        bill_btn = Button(F1, text="Search",command=find_bill,width=10, font=("times new roman", 18, "bold"),fg="white",background=bg_color).grid(row=0, column=6,
                                                                                                  padx=10, pady=5)
        def callback(event):
            con = mysql.connector.connect(host="localhost", user="root", password="nikunj22",
                                          database="bill_system")
            cursor = con.cursor(buffered=True)
            a = []
            b=[]
            cursor.execute("select phone_no from bill where name = '" + self.c_name.get() + "';")
            o = cursor.fetchall()
            for i in o:
                a.append(i[0])
            for j in a:
                self.c_no.set(j)
            cursor.execute("select bill_no from bill where name = '" +self.c_name.get()+"';")
            o1=cursor.fetchall()
            for i1 in o1:
                b.append((i1[0]))
            for j1 in b:
                self.search_bill.set(j1)
        root.bind('<Return>', callback)

        # ========Bill Area======================
        F2 = Frame(self.root, bd=10, relief=GROOVE,background=bg_color)
        F2.place(x=985, y=180, width=350, height=360)
        bill_title = Label(F2, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE,fg="white",background=bg_color).pack(fill=X)
        scroll_y = Scrollbar(F2, orient=VERTICAL)
        self.txtarea = Text(F2,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack()
        welcome_bill()

        def ta():
            return str(self.txtarea.get("1.0",'end-1c'))

        # ======Button Frame======================
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),fg="white",background=bg_color)
        F3.place(x=0, y=540, relwidth=1, height=140)

        btn_frame = Frame(F3, bd=7, relief=GROOVE,background=bg_color)
        btn_frame.place(x=650, width=675, height=105)

        m1 = Label(F3, text="Total Groceries price", font=("times new roman", 20, "bold",),fg="white",background=bg_color,width=20).grid(row=0, column=1, pady=10,
                                                                                           padx=10)
        m1_txt = Entry(F3, textvariable=self.total_grocery_price,font=("times new roman", 13, "bold"), bd=5, relief=GROOVE,fg="white",background=bg_color).grid(row=0, column=2, pady=10,
                                                                                           padx=10)

        m2 = Label(F3, text="Groceries Tax", font=("times new roman", 20, "bold",),fg="white",background=bg_color,width=20).grid(row=1, column=1, pady=10,
                                                                                           padx=10)
        m2_txt = Entry(F3, textvariable=self.grocery_tax,font=("times new roman", 13, "bold"), bd=5, relief=GROOVE,fg="white",background=bg_color).grid(row=1, column=2, pady=10,
                                                                                           padx=10)

        total_btn = Button(btn_frame, text="Total", command=total,pady=10, width=11, font="arial 12 bold",fg="white",background=bg_color).grid(row=0, column=0,
                                                                                                  padx=5, pady=10)
        Gbill_btn = Button(btn_frame, text="Generate Bill", command=bill_area,pady=10, width=11, font="arial 12 bold",fg="white",background=bg_color).grid(row=0,column=1,
                                                                                                          padx=5,pady=10)
        message_btn = Button(btn_frame, text="WhatsApp", pady=10, width=11, font="arial 12 bold",fg="white",background=bg_color,command=message).grid(row=0,
                                                                                                        column=2, padx=5,
                                                                                              pady=10)
        clear_btn = Button(btn_frame, text="Clear", command=clear,pady=10, width=11, font="arial 12 bold",fg="white",background=bg_color).grid(row=0, column=3,
                                                                                                  padx=5, pady=10)
        Exit_btn = Button(btn_frame, text="Exit", pady=10, width=11, font="arial 12 bold",command=exit,fg="white",background=bg_color).grid(row=0, column=4, padx=5,pady=10)

        # ======Groceries Frame=============
        F4 = LabelFrame(self.root, text="Groceries", font=("times new roman", 15, "bold"),fg="white",background=bg_color)
        F4.place(x=5, y=170, width=965, height=360)

        apple = Label(F4, text="Apples", font="arial 15 bold",fg="white",background=bg_color).grid(row=0, column=0, pady=10, padx=10)
        e1 = Entry(F4, width=10, textvariable=self.apple,font=("times new roman", 16, "bold"), bd=5, relief=GROOVE,fg="white",background=bg_color).grid(row=0, column=1,
                                                                                                 padx=10, pady=10)

        banana = Label(F4, text="Bananas", font="arial 15 bold",fg="white",background=bg_color).grid(row=1, column=0, pady=10, padx=10)
        e2 = Entry(F4, width=10, textvariable=self.banana,font=("times new roman", 16, "bold"), bd=5, relief=GROOVE,fg="white",background=bg_color).grid(row=1, column=1,
                                                                                                 padx=10, pady=10)

        berries = Label(F4, text="Frozen Berries", font="arial 15 bold",fg="white",background=bg_color).grid(row=2, column=0, pady=10, padx=10)
        e3 = Entry(F4, width=10, textvariable=self.berries,font=("times new roman", 16, "bold"), bd=5, relief=GROOVE,fg="white",background=bg_color).grid(row=2, column=1,
                                                                                                 padx=10, pady=10)

        yogurd = Label(F4, text="Greek Yogurd", font="arial 15 bold",fg="white",background=bg_color).grid(row=3, column=0, pady=10, padx=10)
        e4 = Entry(F4, width=10, textvariable=self.yogurd,font=("times new roman", 16, "bold"), fg="white",background=bg_color,bd=5, relief=GROOVE).grid(row=3, column=1,
                                                                                                 padx=10, pady=10)

        milk = Label(F4, text="Almond milk", font="arial 15 bold",fg="white",background=bg_color).grid(row=4, column=0, pady=10, padx=10)
        e5 = Entry(F4, width=10, textvariable=self.milk,font=("times new roman", 16, "bold"), fg="white",background=bg_color,bd=5, relief=GROOVE).grid(row=4, column=1,
                                                                                                 padx=10, pady=10)

        oil = Label(F4, text="Olive oil", font="arial 15 bold",fg="white",background=bg_color).grid(row=5, column=0, pady=10, padx=10)
        e6 = Entry(F4, width=10, textvariable=self.oil,font=("times new roman", 16, "bold"), fg="white",background=bg_color,bd=5, relief=GROOVE).grid(row=5, column=1,
                                                                                                 padx=10, pady=10)

        avocado = Label(F4, text="Avacado", font="arial 15 bold",fg="white",background=bg_color).grid(row=0, column=2, pady=10, padx=10)
        e7 = Entry(F4, width=10, textvariable=self.avocado,font=("times new roman", 16, "bold"), fg="white",background=bg_color,bd=5, relief=GROOVE).grid(row=0, column=3,
                                                                                                 padx=10, pady=10)

        salmon = Label(F4, text="Frozen Salmon", font="arial 15 bold",fg="white",background=bg_color).grid(row=1, column=2, pady=10, padx=10)
        e8 = Entry(F4, width=10, textvariable=self.salmon,font=("times new roman", 16, "bold"), fg="white",background=bg_color,bd=5, relief=GROOVE).grid(row=1, column=3,
                                                                                                 padx=10, pady=10)

        eggs = Label(F4, text="Eggs", font="arial 15 bold",fg="white",background=bg_color).grid(row=2, column=2, pady=10, padx=10)
        e9 = Entry(F4, width=10, textvariable=self.eggs,font=("times new roman", 16, "bold"), fg="white",background=bg_color,bd=5, relief=GROOVE).grid(row=2, column=3,
                                                                                                 padx=10, pady=10)

        chicken = Label(F4, text="Chicken", font="arial 15 bold",fg="white",background=bg_color).grid(row=3, column=2, pady=10, padx=10)
        e10 = Entry(F4, width=10, textvariable=self.chicken,font=("times new roman", 16, "bold"), fg="white",background=bg_color,bd=5, relief=GROOVE).grid(row=3, column=3,
                                                                                                  padx=10, pady=10)

        chickpeas = Label(F4, text="Chickpeas", font="arial 15 bold",fg="white",background=bg_color).grid(row=4, column=2, pady=10, padx=10)
        e11 = Entry(F4, width=10, textvariable=self.chickpeas,font=("times new roman", 16, "bold"), fg="white",background=bg_color,bd=5, relief=GROOVE).grid(row=4, column=3,
                                                                                                  padx=10, pady=10)

        lettuce = Label(F4, text="lettuce", font="arial 15 bold",fg="white",background=bg_color).grid(row=5, column=2, pady=10, padx=10)
        e12 = Entry(F4, width=10, textvariable=self.lettuce,font=("times new roman", 16, "bold"), fg="white",background=bg_color,bd=5, relief=GROOVE).grid(row=5, column=3,
                                                                                                  padx=10, pady=10)

        zucchini = Label(F4, text="Zucchini", font="arial 15 bold",fg="white",background=bg_color).grid(row=0, column=4, pady=10, padx=10)
        e13 = Entry(F4, width=10, textvariable=self.zucchini,font=("times new roman", 16, "bold"), fg="white",background=bg_color,bd=5, relief=GROOVE).grid(row=0, column=5,
                                                                                                  padx=10, pady=10)

        cucumber = Label(F4, text="Cucumber", font="arial 15 bold",fg="white",background=bg_color).grid(row=1, column=4, pady=10, padx=10)
        e14 = Entry(F4, width=10, textvariable=self.cucumber,font=("times new roman", 16, "bold"), fg="white",background=bg_color,bd=5, relief=GROOVE).grid(row=1, column=5,
                                                                                                  padx=10, pady=10)

        brocoli = Label(F4, text="Frozen Brocoli", font="arial 15 bold",fg="white",background=bg_color).grid(row=2, column=4, pady=10, padx=10)
        e15 = Entry(F4, width=10, textvariable=self.brocoli,font=("times new roman", 16, "bold"), fg="white",background=bg_color,bd=5, relief=GROOVE).grid(row=2, column=5,
                                                                                                  padx=10, pady=10)

        carrot = Label(F4, text="Carrots", font="arial 15 bold",fg="white",background=bg_color).grid(row=3, column=4, pady=10, padx=10)
        e16 = Entry(F4, width=10, textvariable=self.carrot,font=("times new roman", 16, "bold"), fg="white",background=bg_color,bd=5, relief=GROOVE).grid(row=3, column=5,
                                                                                                  padx=10, pady=10)

        rice = Label(F4, text="Brown Rice", font="arial 15 bold",fg="white",background=bg_color).grid(row=4, column=4, pady=10, padx=10)
        e17 = Entry(F4, width=10, textvariable=self.rice,font=("times new roman", 16, "bold"), fg="white",background=bg_color,bd=5, relief=GROOVE).grid(row=4, column=5,
                                                                                                  padx=10, pady=10)

        Qatmeal = Label(F4, text="Qatmeal", font="arial 15 bold",fg="white",background=bg_color).grid(row=5, column=4, pady=10, padx=10)
        e18 = Entry(F4, width=10, textvariable=self.Qatmeal,font=("times new roman", 16, "bold"), fg="white",background=bg_color,bd=5, relief=GROOVE).grid(row=5, column=5,
                                                                                                  padx=10, pady=10)


root = Tk()
obj = BillApp(root)
root.mainloop()