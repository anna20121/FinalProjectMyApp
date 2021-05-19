import matplotlib.pyplot as plt
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from tkcalendar import *  # installed
import sqlite3
import random
import requests
import pandas as pd
from matplotlib.pyplot import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib
matplotlib.use('TkAgg')  # choose backend


root = Tk()
root.geometry("500x200")
root.title('ALfa team App')
frame = Frame(root,)

# --------Labels--------
userLabel = Label(frame, text="Name")
userLabel.grid(row=1, column=0,)
PasswordLabel = Label(frame, text="Password")
PasswordLabel.grid(row=2, column=0, )

# -------Entrys data--------
userName = Entry(frame, width=35, )
userName.grid(row=1, column=1, padx=10, pady=5)
Password = Entry(frame, width=35,show='*', bd=2)
Password.grid(row=2, column=1, padx=5, pady=10)

#--------- functions are place here ------------
def time():
#--------- current date and time----------------
    now = datetime.now()
    date_time = now.strftime("%I:%M:%S")
    time_label.config(text=date_time)
# ----------loging verfy----------
def login():
    suffix = []
    user = userName.get()
    passw = Password.get()
    userName.delete(0, END)
    Password.delete(0, END)
    list_of_files = os.listdir() 
    for i in list_of_files:
        r_i = i.split('.')
        suffix.append(r_i[0])
    if(user in suffix):
        user_file = open(str(user+".txt"), "r")
        verify = user_file.read().splitlines()
        print(verify)
        if(passw in verify):
            open_mainwindow()

# --------All the data update here------- 
def update_Amount():
    conn = sqlite3.connect('Money.db')
    c = conn.cursor()
    c.execute("SELECT Balance FROM Account")
    records = c.fetchall()
    totalBalancevar = str(''.join(map(str, records[0])))
    conn.commit()
    amount_label['text'] = "Money in the bank "+totalBalancevar+"$"
    amount_label.after(2000, update_Amount)
    conn.close()

def show_frame(frame):
    frame.tkraise()

#Using many windows and combinding 
def combobind(event):

    top = Frame(showWindow, width=480, height=380)
    top.place(x=100, y=100)
    if(int(dateCombo.current()) < 10):
        date = int(dateCombo.current())+1
    date = str(date)
    fig = matplotlib.pyplot.Figure(figsize=(7, 5), dpi=65)
#---create matplotlib canvas using fig and assign to widget top-----
    canvas = FigureCanvasTkAgg(fig, top)
    # get canvas as tkinter widget and put in widget top
    canvas.get_tk_widget().pack()
    conn = sqlite3.connect('Money.db')
    c = conn.cursor()
#--Connecting data entery of cost--
#----Rent----------------------------
    c.execute("select sum(amount) from wallet where substr(date,0,2) =(?) and CATEGORY='Rent' and TYPE=0 ", (date))
    records_rent = c.fetchall()
    if(not all(records_rent[0])):
        total_bal_rent = 0
    else:
        total_bal_rent = int(''.join(map(str, records_rent[0])))
#----Travel--------------------------
    c.execute("select sum(amount) from wallet where substr(date,0,2) =(?) and CATEGORY='Travel' and TYPE=0", (date))
    records_travel = c.fetchall()
    if(not all(records_travel[0])):
        total_bal_travel = 0
    else:
        total_bal_travel = int(''.join(map(str, records_travel[0])))
#----Grocories----------------------
    c.execute("select sum(amount) from wallet where substr(date,0,2) =(?) and CATEGORY='Grocereis' and TYPE=0", (date))
    records_groc = c.fetchall()
    if(not all(records_groc[0])):
        total_bal_groc = 0
    else:
        total_bal_groc = int(''.join(map(str, records_groc[0])))
#----Subscriptions------------------
    c.execute("select sum(amount) from wallet where substr(date,0,2) =(?) and CATEGORY='Subscription' and TYPE=0", (date))
    records_subs = c.fetchall()
    if(not all(records_subs[0])):
        total_bal_subs = 0
    else:
        total_bal_subs = int(''.join(map(str, records_subs[0])))
#----Guilty Pleasures---------------
    c.execute("select sum(amount) from wallet where substr(date,0,2) =(?) and CATEGORY='Guilty Pleasure'and TYPE=0", (date))
    records_guilty = c.fetchall()
    if(not all(records_guilty[0])):
        total_bal_guilty = 0
    else:
        total_bal_guilty = int(''.join(map(str, records_guilty[0])))
#----Show subplot------------------
    ax1 = fig.add_subplot(111)
    df = pd.DataFrame({'X': ['Rent', 'Travel', 'Grocereis',
                             'Subscription', 'Guilty Pleasure'], 'Y': [total_bal_rent, total_bal_travel, total_bal_groc, total_bal_subs, total_bal_guilty]})
    df.plot.bar(x='X', y='Y', ax=ax1)
#-----Transfer all data with all new update happing here---------
def show_summary():
    global showWindow
    showWindow = Tk()
    showWindow.geometry("750x500")
    showWindow.title('Alfa team App')
    global combodatevar
    global dateCombo
    combodatevar = StringVar()
    catLabel = Label(showWindow, text="Month", font=("Arial Bold", 10))
    catLabel.place(x=200, y=60, )
    dateCombo = ttk.Combobox(showWindow, width=25, textvariable=combodatevar)
    dateCombo['values'] = ['January', 'February', 'March', 'April', 'May',
                           'June', 'August', "September", 'October', 'November', 'December']
    dateCombo.place(x=270, y=60, )
    dateCombo.bind("<<ComboboxSelected>>", combobind)
    logoutBtn = Button(showWindow, text="Logout",height=1, width=15, font="Helvetica", command=mainWindow.quit)
    logoutBtn.place(x=580, y=320)
    returnBtn = Button(showWindow, text="return", height=1, width=15, font="Helvetica", command=showWindow.destroy)
    returnBtn.place(x=580, y=280)
#-----Using sqlite and maping the data-----------------------------
    conn = sqlite3.connect('Money.db')
    c = conn.cursor()
    c.execute("select sum(amount) from wallet where TYPE=0")
    records_spend = c.fetchall()
    tot_spend = int(''.join(map(str, records_spend[0])))  
    c.execute("select sum(amount) from wallet where TYPE=1")
    records_in = c.fetchall()
    tot_in = int(''.join(map(str, records_in[0])))
    conn.commit()
    conn.close()
    tot_saving = (tot_in-tot_spend)
#-----Using sqlite and maping the data spending-----------------
    spendingLabel = Label(showWindow, text="Spending: " + str(tot_spend), )
    spendingLabel.place(x=580, y=160)
    MoneyinLabel = Label(showWindow, text="Money in: " + str(tot_in), )
    MoneyinLabel.place(x=580, y=140, )
    savingLabel = Label(showWindow, text="Saving in: " + str(tot_saving), )
    savingLabel.place(x=580, y=120, )
#-----In this code saving and update data happing-------------
def update_savings():
    f = open("savings.txt", 'w')
    open("savings.txt", 'w').close()
    f.write("saving " + str(savingEntry.get()))
    f.write("\n")
    f.write("target " + str(targetLabelEntry.get()))
    f.write("\n")
    f.write("monthly " + str(monthlyEntry.get()))
    messagebox.showinfo(
        title="Successful", message="Changes Made")
    f.close()
#-----Using rundom number game for lotto---------------------
def play_lotto():
    val = 7
    conn = sqlite3.connect('Money.db')
    c = conn.cursor()
    c.execute("SELECT Balance FROM Account")
    records = c.fetchall()
    totbalance = int(''.join(map(str, records[0])))
    totbalance = totbalance + (100*val)
    c.execute("""UPDATE Account SET Balance=:balance WHERE id = :Id """, { 'balance': totbalance,'Id': 1 } )
    conn.commit()
    conn.close()
    messagebox.showinfo(
        title="Lotto", message="Gambling is stupid you have won nothing")
#-----Making Wallet to collecting data------------
def sub_fnc():
    conn = sqlite3.connect('Money.db')
    if(amountvar.get() and datevar.get() and catvar.get()):
        amount = int(amountvar.get())
        c = conn.cursor()
        c.execute("Insert INTO wallet(DATE,AMOUNT,CATEGORY,TYPE) VALUES(:date,:amount,:category,:type)",
                  {'date': datevar.get(),'amount': amountvar.get(),'category': catvar.get(),'type': var.get()})
        c.execute("SELECT Balance FROM Account")
        records = c.fetchall()
        totbalance = int(''.join(map(str, records[0])))# map is used to find plase for data  
        if(var.get() == 0):
            totbalance = totbalance - amount
        else:
            totbalance = totbalance + amount
        c.execute("""UPDATE Account SET Balance=:balance WHERE id = :Id """,
                  {'balance': totbalance,'Id': 1 })
        messagebox.showinfo(title="Successful", message="Transaction Successful")
        amountEntry.delete(0, END)
    else:
        messagebox.showwarning(title="Warning", message="Please Fillup")
    conn.commit()
    conn.close()
#----This code can handel two frames------
def raise_frm(frame_1, frame_2):
    frame_1.tkraise()
    frame_2.tkraise()
#----Using all data we used golbal to make sure all callect----
def open_mainwindow():
    global clockBtn
    global amountEntry
    global DateEntry
    global mainWindow
    root.destroy()
#----New data frame----------------------
    mainWindow = Tk()
    mainWindow.geometry("950x500")
    mainWindow.title('Alfa team App')
#----Menu frame--------------------------
    my_menu = Menu(mainWindow)
    mainWindow.config(menu=my_menu)
#----MenuItems---------------------------
#-----------File-------------------------
    file_menu = Menu(my_menu)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command=mainWindow.quit)
    edit_menu = Menu(my_menu)
    my_menu.add_cascade(label="Edit", menu=edit_menu)
#----Frames data-------------------------
    frame_add = Frame(mainWindow, width=280, height=480,)
    frame_add_v2 = Frame(mainWindow, width=280, height=480,)
#-------------------------------Frames-----------------------
    frame_middle_1 = Frame(mainWindow, width=590, height=480,)
    frame_middle_2 = Frame(mainWindow, width=590, height=480,)
    frame_middle_3 = Frame(mainWindow, width=590, height=480,)
#----Frame condetions--------------------
    for frame in (frame_middle_1, frame_middle_2, frame_middle_3):
        frame.grid(row=0, column=1, padx=10, pady=10, sticky='nw')
        frame.grid_propagate(False)
    for frame in (frame_add, frame_add_v2):
        frame.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
        frame.grid_propagate(False)
    show_frame(frame_middle_1)
    show_frame(frame_add)

#----Open weather---------------------------------------------
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
        "Valkeakoski"+"&appid=e53f06c4d248fd8ab5e7c6ab0b8213ac"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    final_info = condition + "\n" + "Valkeakoski" + "\n" +\
        str(temp) + "°C"+"\n" + "Pressure(pa): " + \
        str(pressure) + "\n" + "humidity: " + str(humidity)
    weatherLabel = Label(frame_middle_1, text="Weather condtion "+final_info+"", font=('Arial Bold', 12))
    weatherLabel.grid(row=0, column=0, pady=(120, 0), padx=20, ipadx=10, ipady=10,)
#----Frame 2 and condition-----------------
    global var
    global catvar
    global amountvar
    global datevar
    var = IntVar()
    datevar = StringVar()
    catvar = StringVar()
    amountvar = StringVar()
    catLabel = Label(frame_middle_2, text="Category", font=("Arial Bold", 10))
    catLabel.grid(row=0, column=0, pady=(100, 20), padx=(20, 10))
    categoryCombo = ttk.Combobox(frame_middle_2, width=30, height=10, textvariable=catvar)
    categoryCombo['values'] = ['Rent', 'Travel','Groceries', 'Subscription', 'Guilty Pleasures']
    categoryCombo.current(0)
    categoryCombo.grid(row=0, column=1, pady=(100, 20), padx=10, ipadx=5)
    amountLabel = Label(frame_middle_2, text="Amount",font=("Arial Bold", 10))
    amountLabel.grid(row=1, column=0, pady=(0, 20), padx=(20, 10))
    amountEntry = Entry(frame_middle_2, width=35, bd=5, textvariable=amountvar)
    amountEntry.grid(row=1, column=1, pady=(0, 10), padx=10)
    dateLabel = Label(frame_middle_2, text="Date",font=("Arial Bold", 10))
    dateLabel.grid(row=2, column=0, pady=(0, 10), padx=(20, 10))
    dateEntry = Entry(frame_middle_2, width=35, bd=5, textvariable=datevar)
    dateEntry.insert(0, "Enter manual date or use picker")
    dateEntry.grid(row=2, column=1, pady=(0, 10), padx=10)
    moneyLabel = Label(frame_middle_2, text="Money in?",font=("Arial Bold", 10))
    moneyLabel.grid(row=3, column=0, pady=(0, 10), padx=(20, 10))
    moneyBox = Checkbutton(frame_middle_2, variable=var, fg="#05ab0d",)
    moneyBox.grid(row=3, column=1, pady=(0, 20), padx=5, sticky='w')

#----Buttons-------------------

    logoutBtn = Button(frame_middle_1, text="Logout",height=1, width=15, font="Helvetica", command=mainWindow.quit)
    logoutBtn.grid(row=0, column=2, pady=5, padx=100)

    transacBtn = Button(frame_middle_1, text="Add Transaction",height=1, width=15, font="Helvetica", command=lambda: show_frame(frame_middle_2))
    transacBtn.grid(row=1, column=2, pady=5, padx=100)

    editBtn = Button(frame_middle_1, text="Edit account", height=1, width=15, font="Helvetica", )
    editBtn.grid(row=2, column=2, pady=5, padx=100)

    setupBtn = Button(frame_middle_1, text="Setup", height=1, width=15, font="Helvetica", command=lambda: raise_frm(frame_add_v2, frame_middle_3))
    setupBtn.grid(row=3, column=2, pady=5, padx=100)

    summaryBtn = Button(frame_middle_1, text="Account Summary", height=1, width=15, font="Helvetica", command=show_summary)
    summaryBtn.grid(row=4, column=2, pady=5, padx=100)
    playBtn = Button(frame_middle_1, text="Play Lotto",height=1, width=15, font="Helvetica", command=play_lotto)
    playBtn.grid(row=5, column=2, pady=5, padx=100)
    clockBtn = PhotoImage(file='images/clock.png')
    getTimeBtn = Button(frame_add, image=clockBtn, border=0,command=time)
    getTimeBtn.grid(row=0, column=0, pady=20, padx=5, sticky="ew")

#----Frame 2 buttons-------------- 
    logoutBtn_2 = Button(frame_middle_2, text="Logout", height=1, width=15, font="Helvetica", command=mainWindow.quit)
    logoutBtn_2.grid(row=0, column=3, pady=(100, 20), padx=100)
    transacBtn_2 = Button(frame_middle_2, text="Add Transaction",height=1, width=15, font="Helvetica", command=sub_fnc)
    transacBtn_2.grid(row=1, column=3, pady=(0, 20), padx=100)
    canelBtn = Button(frame_middle_2, text="Cancel and return", height=1, width=15, font="Helvetica", command=lambda: show_frame(frame_middle_1))
    canelBtn.grid(row=2, column=3, pady=(0, 20), padx=100)

#----Frame 3 buttons--------------
    logoutBtn_3 = Button(frame_middle_3, text="Logout", height=1, width=15, font="Helvetica", command=mainWindow.quit)
    logoutBtn_3.grid(row=0, column=3, pady=(100, 20), padx=50)

    acceptBtn = Button(frame_middle_3, text="Accept Changes", height=1, width=15, font="Helvetica", command=update_savings)
    acceptBtn.grid(row=1, column=3, pady=(0, 20), padx=50)
    returnBtn = Button(frame_middle_3, text="Return", height=1, width=15, font="Helvetica", command=lambda: show_frame(frame_middle_1))
    returnBtn.grid(row=2, column=3, pady=(0, 20), padx=50)    

#----Account Summary (table and save data)------------
    global savingEntry
    global targetLabelEntry
    global monthlyEntry
    f = open("savings.txt", 'r')
    filedata = f.read()
    print(filedata.splitlines())
    x = []
    y = []
    for line in open("savings.txt", "r").readlines():  # Read the lines
        # Split on the space, and store the results in a list of two strings
        info = line.split()
        print(info)
        x.append(info[0])
        y.append(info[1])
    savingLabel = Label(frame_middle_3, text="Saving Target",)
    savingLabel.grid(row=0, column=0, pady=(150, 20), padx=(20, 10))
    savingEntry = Entry(frame_middle_3, width=30,)
    savingEntry.grid(row=0, column=1, pady=(150, 20), ipadx=5)
    savingEntry.insert(0, y[0])
    targetLabel = Label(frame_middle_3, text="target", )
    targetLabel.grid(row=1, column=0, pady=(0, 20), padx=(20, 10),)
    targetLabelEntry = Entry(frame_middle_3, width=30,)
    targetLabelEntry.grid(row=1, column=1, pady=(0, 20), ipadx=5)
    targetLabelEntry.insert(0, y[1])
    monthlyLabel = Label(frame_middle_3, text="Budget",)
    monthlyLabel.grid(row=2, column=0, pady=(0, 20), padx=(20, 10))
    monthlyEntry = Entry(frame_middle_3, width=30,)
    monthlyEntry.grid(row=2, column=1, pady=(0, 20), ipadx=5)
    monthlyEntry.insert(0, y[2])

#----Database-------------------
#--------------Time Label---------------------------
    global time_label
    time_label = Label(frame_add, font=("Arial", 10))
    time_label.grid(row=1, column=0, pady=5, padx=20,)
    global amount_label
    amount_label = Label(
        frame_middle_1, font=('Arial Bold', 12))
    amount_label.grid(row=1, column=0, pady=(0, 5), padx=20, ipadx=10, ipady=10,)
#----Calender-------------------
#cal = Calendar(frame_add, selectmode="day", font="Arial 8", 
                   #locale="fi_FI", disabledforeground="red",
                   #cursor="hand")
    cal = Calendar(frame_add, selectmode="day", year=2021,
                  month=5, day=4, textvariable=datevar)
    cal.grid(row=2, column=0, pady=20, padx=20, )
    update_Amount()
    conn.close()
#----conecting SQL table---------
conn = sqlite3.connect('Money.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS wallet(
       ID INTEGER PRIMARY KEY AUTOINCREMENT,
   DATE           TEXT,
   AMOUNT         INT,
   CATEGORY       TEXT,
   TYPE           INT)""")
c.execute("""CREATE TABLE IF NOT EXISTS Account(id int UNIQUE,Balance INTEGER  )""")

c.execute("Insert or IGNORE INTO Account VALUES(:id,:balance)",{'id': 1,'balance': 1000})
conn.commit()
#----Logging Button function------
loginBtn = Button(frame, text="login",height=1, width=5, font="Tahoma", command=open_mainwindow)
loginBtn.grid(row=3, column=0, pady=5)

frame.place(relx=0.1, rely=0.1)
conn.close()
root.mainloop()
