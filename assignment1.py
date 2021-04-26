# these are Module used in the Program
from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3 as sql


# it give Database connection
class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sql.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


def createOrderTable():
    with DatabaseConnection('Database.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE Orders(order_id integer,no_of_item integer,price integer)')


def Submit():
    try:
        for widget in f.winfo_children():
            widget.destroy()
    except:
        pass

    List = [int(a.get()), int(b.get()), int(c.get())]

    with DatabaseConnection('Database.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Orders VALUES(?,?,?)', (List[0], List[1], List[2]))

    Summary()


def Summary():
    with DatabaseConnection('Database.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Orders')
        v = cursor.fetchall()
    msg = 'S.no.\t\tOrder ID\t\tNo. of Items\t\tPrice\t\tTotal'
    l2 = Label(win,text=msg).grid(column = 0,row =9)
    j = 10
    to=0
    ti=0
    tp=0
    for i in v:
        to+=1
        ti+=i[1]
        tp +=i[1]*i[2]

        msg = str(j-9) +'.\t\t' + str(i[0]) + '\t\t' + str(i[1]) +'\t\t' + str(i[2]) + '\t\t' + str(i[1]*i[2])
        l1 = Label(win,text=msg).grid(column=0,row=j)
        j+=1

    msg = 'Total ' + '\t\t' +str(to) + '\t\t' + str(ti) + '\t\t'  + '\t\t' + str(tp)
    l1 = Label(win, text=msg).grid(column=0, row=j)



# try to Create Table
try:
    createOrderTable()
except:
    pass

# main code
win = Tk()
win.geometry('1000x1000+50+50')
win.title("Graphical Hotel Reservation")

# temporary Frame
f = Frame(win)
f.grid(column=0, row=40)

l00 = Label(win, text='Order', fg='Blue')
l00.config(font=('TimesNewRoman', 20))
l00.grid(column=15, row=0)

# Gui for Add an entry
a = StringVar()
b = StringVar()
c = StringVar()

l1 = Label(win, text='Order ID ').grid(column=0, row=2)
e1 = Entry(win, width=20, textvariable=a).grid(column=10, row=2)

l2 = Label(win, text='Number of Items ').grid(column=20, row=2)
e2 = Entry(win, width=20, textvariable=b).grid(column=30, row=2)

l3 = Label(win, text='Price ').grid(column=0, row=4)
e3 = Entry(win, width=20, textvariable=c).grid(column=10, row=4)

b2 = Button(win, text="Submit", command=Submit).grid(column=30, row=4)

b3 = Button(win, text="Summary", command=Summary).grid(column=18, row=6)

win.mainloop()