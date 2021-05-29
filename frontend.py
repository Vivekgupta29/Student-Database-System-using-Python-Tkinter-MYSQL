from tkinter import *
import tkinter.messagebox
import project1_backend as bkend
import mysql.connector


window=Tk()
window.title("Student Database Management System")
window.geometry("1350x750+0+0")
# window.state("zoomed")
# window.config(bg="sky blue")
aicon = PhotoImage(file = r"icons/add.png")
sicon = PhotoImage(file = r"icons/search.png")

stdid = StringVar()
name = StringVar()
rollno = StringVar()
dob = StringVar()
gender = StringVar()
address = StringVar()
mobile = StringVar()


mainframe=Frame(window,bg="cadet blue")
mainframe.grid()

f1 = Frame(mainframe, width=800, relief=RIDGE)
f1.pack(side=TOP)
# relief types=== FLAT RAISED SUNKEN GROOVE RIDGE


f4 = Frame(mainframe, width=1300,height=400,relief=RIDGE)
f4.pack(side=BOTTOM,padx=5,pady=10)

f2 = LabelFrame(mainframe, width=800,font=('ARIAL', 40, 'bold'),fg="red",text="Student info", relief=RIDGE)
f2.pack(side=LEFT,pady=15)

f3 = LabelFrame(mainframe, width=800,font=('ARIAL', 40, 'bold'),fg="red",text="Details", relief=RIDGE)
f3.pack(side=RIGHT)


label1 = Label(f1, font=('ARIAL', 40, 'bold'),
                text="Student Management System",
                fg="BLUE", bd=10, anchor='w')

label1.grid()


# stdid
lbl2 = Label(f2, font=('arial', 16, 'bold'),
               text="StdID", bd=16, anchor="w")
lbl2.grid(row=2, column=0)
# stdid Entry box
txtstdid = Entry(f2, font=('arial', 16, 'bold'),
               textvariable=stdid, bd=6,
               bg="white", justify='left')
txtstdid.grid(row=2, column=1)


#name
lbl3 = Label(f2, font=('arial', 16, 'bold'),
               text="Name", bd=16, anchor="w")
lbl3.grid(row=3, column=0)
# name Entry box
txtname = Entry(f2, font=('arial', 16, 'bold'),
               textvariable=name, bd=6,
               bg="white", justify='left')
txtname.grid(row=3, column=1)


# rollno
lbl4 = Label(f2, font=('arial', 16, 'bold'),
                  text="Rollno", bd=16, anchor="w")
lbl4.grid(row=4, column=0)
# rollno entry box
txtrollno = Entry(f2, font=('arial', 16, 'bold'),
                  textvariable=rollno,bd=8,
                  bg="white", justify='left')
txtrollno.grid(row=4, column=1)

#gender
lbl5 = Label(f2, font=('arial', 16, 'bold'),
                  text="Gender", bd=16, anchor="w")
lbl5.grid(row=5, column=0)
#gender entry box
txtgender = Entry(f2, font=('arial', 16, 'bold'),
                  textvariable=gender,bd=8,
                  bg="white", justify='left')
txtgender.grid(row=5, column=1)


#dob
lbl6 = Label(f2, font=('arial', 16, 'bold'),
                  text="DOB", bd=16, anchor="w")
lbl6.grid(row=6, column=0)
# dob Entry
txtdob = Entry(f2, font=('arial', 16, 'bold'),
                  textvariable=dob,bd=8,
                  bg="white", justify='left')
txtdob.grid(row=6, column=1)


#address
lbl7 = Label(f2, font=('arial', 16, 'bold'),
                  text="Address", bd=16, anchor="w")
lbl7.grid(row=7, column=0)
# address Entry
txtaddress = Entry(f2, font=('arial', 16, 'bold'),
                  textvariable=address,bd=8,
                  bg="white", justify='left')
txtaddress.grid(row=7, column=1)


#mobile
lbl8 = Label(f2, font=('arial', 16, 'bold'),
                  text="Mobile", bd=16, anchor="w")
lbl8.grid(row=8, column=0)
# mobile Entry
txtmobile = Entry(f2, font=('arial', 16, 'bold'),
                  textvariable=mobile,bd=8,
                  bg="white", justify='left')
txtmobile.grid(row=8, column=1)





scrollbar=Scrollbar(f3)

studentlist=Listbox(f3,font=('arial',12,'bold'),yscrollcommand=scrollbar.set,width=41,height=16)

studentlist.grid(row=1,column=0,padx=8)

scrollbar.grid(row=1,column=1,sticky='ns')
scrollbar.config(command=studentlist.yview)

lbl10 = Label(f3, font=('arial', 8, 'bold'),fg="red",
                  text="", bd=16, anchor="w")
lbl10.grid(row=2, column=0)

def Exit1():
    Exit1=tkinter.messagebox.askyesno("Database System","Confirm if you want to Exit or not")
    if Exit1 > 0:
        window.destroy()
        return

def clearData():
    txtstdid.delete(0,END)
    txtname.delete(0,END)
    txtrollno.delete(0,END)
    txtdob.delete(0,END)
    txtgender.delete(0,END)
    txtaddress.delete(0,END)
    txtmobile.delete(0,END)

def addData():
        # con = mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="project2")
        # cur=con.cursor()
        # cur.execute("select stdid from student where stdid>0")
        # print(stdid)
        # if((stdid.get())==():
        #     print("duplicate values")
        if(len(stdid.get())!=0):
            bkend.addStdRec(stdid.get(),name.get(),rollno.get(),dob.get(),gender.get(),address.get(),mobile.get())
            studentlist.delete(END,0)

            studentlist.insert(END,(stdid.get(),name.get(),rollno.get(),dob.get(),gender.get(),address.get(),mobile.get()))
       
        
    # except mysql.connector.errors.IntegrityError as err:
    #     my_text=err
    #     lbl10.config(text = my_text)
    #     return
        # lbl10[""]=("{}".format(err))
        

def DisplayData():
    studentlist.delete(0,END)
    for row in bkend.viewData():
        studentlist.insert(END,row)

def StudentRec(event):
    global sd
    searchStd=studentlist.curselection()
    sd=studentlist.get(searchStd)
    
    print(sd)
    txtstdid.delete(0,END)
    txtstdid.insert(END,sd[0])

    txtname.delete(0,END)
    txtname.insert(END,sd[1])

    txtrollno.delete(0,END)
    txtrollno.insert(END,sd[2])

    txtdob.delete(0,END)
    txtdob.insert(END,sd[3])

    txtgender.delete(0,END)
    txtgender.insert(END,sd[4])

    txtaddress.delete(0,END)
    txtaddress.insert(END,sd[5])

    txtmobile.delete(0,END)
    txtmobile.insert(END,sd[6])



def DeleteData():
    if(len(stdid.get())!=0):
        # bkend.deleteRec(sd[0])
        bkend.deleteRec(stdid.get())
        clearData()
        DisplayData()

def searchDatabase():
    studentlist.delete(0,END)
    for row in bkend.searchData(stdid.get(),name.get(),rollno.get(),dob.get(),gender.get(),address.get(),mobile.get()):
        studentlist.insert(END, row)

def Update():
    if (len(stdid.get()) != 0):
        bkend.deleteRec(stdid.get())
        # DisplayData()
        bkend.viewData()
        bkend.addStdRec(stdid.get(),name.get(),rollno.get(),dob.get(),gender.get(),address.get(),mobile.get())
        studentlist.delete(END,0)

        studentlist.insert(END, (stdid.get(),name.get(),rollno.get(),dob.get(),gender.get(),address.get(),mobile.get()))
        


# Buttons
btnAddNew = Button(f4, padx=8, pady=6, bd=8,
                  fg="black", font=('arial', 16, 'bold'),
                  width=170, text="ADD NEW", bg="blue",image = aicon,command=addData).grid(row=0, column=0)

btnSearch = Button(f4, padx=8, pady=6, bd=8,
                  fg="black", font=('arial', 16, 'bold'),
                  width=170, text="Search", bg="blue",image = sicon,command=searchDatabase).grid(row=0, column=1)

btnDisplay = Button(f4, padx=8, pady=6, bd=8,
                  fg="black", font=('arial', 16, 'bold'),
                  width=12, text="Display", bg="light green",command=DisplayData).grid(row=0, column=2)

btnclearData = Button(f4, padx=8, pady=6, bd=8,
                  fg="black", font=('arial', 16, 'bold'),
                  width=12, text="Clear Data", bg="light green",command=clearData).grid(row=0, column=3)

btnDelete = Button(f4, padx=8, pady=6, bd=8,
                  fg="black", font=('arial', 16, 'bold'),
                  width=12, text="Delete", bg="light green",command=DeleteData).grid(row=0, column=4)


btnUpdate = Button(f4, padx=8, pady=6, bd=8,
                  fg="black", font=('arial', 16, 'bold'),
                  width=12, text="Update", bg="light green",command=Update).grid(row=0, column=5)

btnExit = Button(f4, padx=8, pady=6, bd=8,
                  fg="black", font=('arial', 16, 'bold'),
                  width=12, text="Exit", bg="red",command=Exit1).grid(row=0, column=6)

studentlist.bind("<<ListboxSelect>>",StudentRec)
window.mainloop()