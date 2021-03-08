import pymysql
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

def create_table():
    db=pymysql.connect(host="localhost",user="root",passwd=rootpwd,db=database)
    cur=db.cursor()
    cur.execute("create table stu(Roll int,Name char(20),Class char(5),English int, Physics int, Chemistry int, Maths int, Computers int, Percentage char(6),Grade char(2), Remark char(4));")
    db.commit()
    cur.close()
    db.close()

def add_record_screen():
    global mainframe
    mainframe.destroy()
    mainframe = Frame(root,width=1100,height=600,bg="#111")
    mainframe.grid_propagate(0)
    mainframe.pack()

    def add_record():
        roll=int(rolle.get())
        name=namee.get()
        clas=clase.get()
        eng=int(enge.get())
        mat=int(mate.get())
        cs=int(cse.get())
        chem=int(cheme.get())
        phy=int(phye.get())
        total = eng+mat+phy+chem+cs
        perc = round(total/500 * 100,2)
        if perc > 33 : rem = 'PASS'
        else: rem = 'FAIL'
        if perc > 90: grade = 'A1'
        elif perc > 80: grade = 'A2'
        elif perc > 70: grade = 'B1'
        elif perc > 60: grade = 'B2'
        elif perc > 50: grade = 'C1'
        elif perc > 40: grade = 'C2'
        elif perc > 33: grade = 'D'
        else: grade = 'F'
        perc = str(perc)+"%"

        db=pymysql.connect(host="localhost",user="root",passwd=rootpwd,db=database)
        cur=db.cursor()
        cur.execute(f"insert into stu values({roll},\"{name}\",\"{clas}\",{eng},{phy},{chem},{mat},{cs},\"{perc}\",\"{grade}\",\"{rem}\");")
        db.commit()
        cur.close()
        db.close()

        rolle.delete(0,'end')
        namee.delete(0,'end')
        clase.delete(0,'end')
        enge.delete(0,'end')
        phye.delete(0,'end')
        cheme.delete(0,'end')
        mate.delete(0,'end')
        cse.delete(0,'end')

    Label(mainframe,bg="#111",fg="#fff",text='Roll No.').grid(row=1,column=1)
    Label(mainframe,bg="#111",fg="#fff",text='Name').grid(row=2,column=1)
    Label(mainframe,bg="#111",fg="#fff",text='Class').grid(row=3,column=1)
    Label(mainframe,bg="#111",fg="#fff",text='English').grid(row=4,column=1)
    Label(mainframe,bg="#111",fg="#fff",text='Physics').grid(row=5,column=1)
    Label(mainframe,bg="#111",fg="#fff",text='Chemistry').grid(row=6,column=1)
    Label(mainframe,bg="#111",fg="#fff",text='Mathematics').grid(row=7,column=1)
    Label(mainframe,bg="#111",fg="#fff",text='Comuper Science').grid(row=8,column=1)

    rolle = Entry(mainframe)
    rolle.grid(row=1,column=2)
    namee = Entry(mainframe)
    namee.grid(row=2,column=2)
    clase = Entry(mainframe)
    clase.grid(row=3,column=2)
    enge = Entry(mainframe)
    enge.grid(row=4,column=2)
    phye = Entry(mainframe)
    phye.grid(row=5,column=2)
    cheme = Entry(mainframe)
    cheme.grid(row=6,column=2)
    mate = Entry(mainframe)
    mate.grid(row=7,column=2)
    cse = Entry(mainframe)
    cse.grid(row=8,column=2)

    Button(mainframe,text="Back",command=Menu).grid(row=9,column=1)
    Button(mainframe,text="Submit",command=add_record).grid(row=9,column=2)

def display():
    global box
    db=pymysql.connect(host="localhost",user="root",passwd=rootpwd,db=database)
    cur=db.cursor()
    rows=cur.execute("select * from stu;")
    rec=cur.fetchall()
    records = """
+----------+-------------------------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|Roll No.  |Name                     |Class     |English   |Physics   |Chemistry |Maths     |CS        |Percentage|Grade     |Remarks   |
+----------+-------------------------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
"""
    for i in rec:
        for j in range(len(i)):
            if j==0: records+="|"
            if j==1: records += "{0:<25}|".format(i[j])
            else:  records += "{0:<10}|".format(i[j])
        records+="\n+----------+-------------------------+----------+----------+----------+----------+----------+----------+----------+----------+----------+\n"
    cur.close()
    db.close() 
    box.configure(state='normal')
    box.insert('end', records)
    box.configure(state='disabled')

def display_graph():
    db=pymysql.connect(host="localhost",user="root",passwd=rootpwd,db=database)
    cur=db.cursor()

    rows=cur.execute("select * from stu;")
    all_records=cur.fetchall()
    avg_eng=avg_phy=avg_chem=avg_maths=avg_cs=0
    for i in all_records:
        avg_eng+=i[3]
        avg_phy+=i[4]
        avg_chem+=i[5]
        avg_maths+=i[6]
        avg_cs+=i[7]

    avg_eng/=rows
    avg_phy/=rows
    avg_chem/=rows
    avg_maths/=rows
    avg_cs/=rows

    bg2=[avg_eng,avg_phy,avg_chem,avg_maths,avg_cs]

    try: rr=int(roll_no.get())
    except:
        print('Please enter roll no.')
        return
    aa=f"select * from stu where roll='{rr}';"
    rows=cur.execute(aa)
    rec=cur.fetchall()

    bg1=[]
    x=["English","Physics","Chemistry","Mathematics","Computer Science"]

    barWidth = 0.1

    for i in rec:
        bg1.append(i[3])
        bg1.append(i[4])
        bg1.append(i[5])
        bg1.append(i[6])
        bg1.append(i[7])

    r1 = np.arange(len(bg1))
    r2 = [i + barWidth for i in r1]

    plt.bar(r1,bg2,width=0.1,label="Class Average")
    plt.bar(r2,bg1,width=0.1,label="Student")
    plt.xlabel('group', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bg1))], ['English', 'Physics', 'Chemistry', 'Maths', 'CS'])

    plt.legend()
    plt.show()
    cur.close()
    db.close()

def Menu():
    global mainframe,box,roll_no
    mainframe.destroy()
    mainframe = Frame(root,width=1100,height=600,bg="#111")
    mainframe.grid_propagate(0)
    mainframe.pack()
    Label(mainframe,text="Menu",bg="#111",fg="#fff",font=('serif',25)).grid(row=1,column=1)
    Button(mainframe,text="Create Table",command=create_table).grid(row=2,column=1)
    Button(mainframe,text="Add Record",command=add_record_screen).grid(row=3,column=1)
    Button(mainframe,text="Display All Records",command=display).grid(row=4,column=1)
    Button(mainframe,text="Display Bar Graph Student Wise",command=display_graph).grid(row=5,column=1)
    Button(mainframe,text="Exit",command=quit).grid(row=6,column=1)
    roll_no = Entry(mainframe)
    roll_no.grid(row=7,column=1)
    box=Text(mainframe,width=137,height=25,bg='#333',fg='#fff',state='disabled')
    box.grid(row=8,column=1)

def connect(a1,a2):
    global database,rootpwd
    rootpwd = a1
    database = a2
    Menu()

def connect_screen():
    e1 = Entry(mainframe,show="*")
    e2 = Entry(mainframe)
    Label(mainframe,text="Enter root@localhost Password",bg="#111",fg="#fff").grid(row=1,column=1)
    e1.grid(row=1,column=2)
    Label(mainframe,text="Enter name of database to be used",bg="#111",fg="#fff").grid(row=2,column=1)
    e2.grid(row=2,column=2)
    Button(mainframe,text="Submit",command=lambda: connect(e1.get(),e2.get()) ).grid(row=3,column=1,columnspan=2)

root = Tk()
root.geometry('1100x600')
mainframe = Frame(root,width=1100,height=600,bg="#111")
mainframe.grid_propagate(0)
mainframe.pack()
connect_screen()
root.mainloop()