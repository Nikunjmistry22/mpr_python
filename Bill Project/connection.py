import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="nikunj22",database="bill_system")
mycursor=mydb.cursor(buffered=True)
a=[]
b=[]
c=[]
def id():
    mycursor.execute("select userid from register;")
    output=mycursor.fetchall()
    for i in output:
         a.append(i[0])
    return a
def password():
    mycursor.execute("select password from register;")
    output1=mycursor.fetchall()
    for i in output1:
        b.append(i[0])
    return b
def name():
    mycursor.execute("select name from bill;")
    output2 = mycursor.fetchall()
    for i in output2:
        c.append(i[0])
    return c

#(id())
#(password())
