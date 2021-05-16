import matplotlib.pyplot as plt
import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
try:
    from tkcalendar import *
except:  #if module was not installed
    import  pip
    pip.main(['install', 'tkcalendar'])
    from tkcalendar import *
from datetime import datetime
import sqlite3
import random
import requests
import calendar
import pandas as pd
from matplotlib.pyplot import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib
matplotlib.use('TkAgg')  # choose backend
import json
import time
import datetime
from time import strftime
  

class AlfaApp(tk.Tk):
 
    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
      # initializing frames to an empty array
        self.frames = {}  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Log_in_Page, MainWindow, CNA, Transactions_Page, Edit_Account, SetUp_Page, Summary_Page):
            frame = F(container, self)
            # initializing frame of that object from
            # startpage, page1, page2... respectively with 
            # for loop
            self.frames[F] = frame 
            frame.grid(row = 0, column = 0, sticky ="nsew")  
        self.show_frame(Log_in_Page)  
        self.title("Alfa App")
        self.geometry("700x500")
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# first window frame - Log In window

class Log_in_Page(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         
        sign = Label(self, text="Login", font=('Arial Bold', 18))
        sign.grid(row=0, column=2, pady=(2, 20))

        userLabel = Label(self, text="Username: ")
        userLabel.grid(row=1, column=1)
        PasswordLabel = Label(self, text="Password: ")
        PasswordLabel.grid(row=2, column=1)

        userName = Entry(self, width=40, bd=3)
        userName.grid(row=1, column=2)
        Password = Entry(self, width=35, show='*', bd=4)
        Password.grid(row=2, column=2)
 
        def verify_login():
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
                  messagebox.showinfo(
                     title="Successful", message="Login Successful")
                  controller.show_frame(MainWindow)
              else:
                  messagebox.showerror(title="Error", message="Wrong Password")
           else:
              messagebox.showerror(title="Error", message="No user found")
    
        LogInButton = ttk.Button(self, text="login", command = verify_login)
        # putting the button in its place by
        # using grid
        LogInButton.grid(row = 3, column = 2, padx = 10, pady = 10)         
        ## button to show frame 2 with text layout2
        CNAbutton = ttk.Button(self, text ="Create New Account",
        command = lambda : controller.show_frame(CNA))
        CNAbutton.grid(row = 4, column = 2, padx = 10, pady = 10)
        #label for clock
        label = Label(self, font=("Courier", 15, 'bold'), bg="navy", fg="white", bd =30)
        label.grid(row =0, column=0, pady=10)
        #clock function
        def digitalclock():
           text_input = time.strftime("%H:%M:%S")
           label.config(text=text_input)
           label.after(200, digitalclock)
        digitalclock()
        self.calendar()
              
    def calendar(self): #creating and placing calendar 
        CalFrame = tk.Frame(self, width=300, height=250)
        CalFrame.grid(row=2, column=0, padx=10)
        cal = Calendar(CalFrame, selectmode="day",
                       background="navy", foreground="white")
        cal.place(width=300, height=250)                 
  
# second window frame MainWindow 

class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # log out
        LogOutB = ttk.Button(self,text="Log Out",
                             command = lambda : controller.show_frame(Transactions))
        LogOutB.grid(row = 1, column = 1, padx = 10, pady = 10)
        # transactions
        AddTrans = ttk.Button(self, text = "Add Transactions",
                              command = lambda : controller.show_frame(Transactions_Page))
        AddTrans.grid(row = 2, column =1, padx = 10, pady = 10)
        # edit account
        editB = ttk.Button(self, text = "Edit Account",
                              command = lambda : controller.show_frame(Edit_Account))
        editB.grid(row = 3, column = 1, padx = 10, pady = 10)
        # set up
        setB = ttk.Button(self, text = "Set up",
                              command = lambda : controller.show_frame(SetUp_Page))
        setB.grid(row = 4, column = 1, padx = 10, pady = 10)
        # account summary
        summB = ttk.Button(self, text = "Summary",
                              command = lambda : controller.show_frame(Summary_Page))
        summB.grid(row = 5, column = 1, padx = 10, pady = 10)
        #play lotto
        lottoB = ttk.Button(self, text = "Play Ltto")
                            #command = lambda : )
        lottoB.grid(row=6, column=1)
        
        
        label = Label(self, font=("Courier", 15, 'bold'), bg="navy", fg="white", bd =30)
        label.grid(row =0, column=0, pady=10)
        #clock function
        def digitalclock():
           text_input = time.strftime("%H:%M:%S")
           label.config(text=text_input)
           label.after(200, digitalclock)
        digitalclock()
        self.calendar()
              
    def calendar(self): #creating and placing calendar 
        CalFrame = tk.Frame(self, width=200, height=150)
        CalFrame.grid(row=3, column=0, padx=10)
        cal = Calendar(CalFrame, selectmode="day",
                       background="navy", foreground="white")
        cal.place(width=200, height=150)
                    
# third windo for Transactions page

class Transactions_Page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        
        conn = sqlite3.connect('Money.db')
        c = conn.cursor()
        
        def add_transaction():
            conn = sqlite3.connect('Money.db')
            c = conn.cursor()
            #c.execute("CREATE TABLE wallet(date TEXT, category TEXT, amount INT)")
            #c.execute("CREATE TABLE Account(balance INT)", {'balance': 100000})
            #c.execute("CREATE TABLE Income(date TEXT, category TEXT, amount INT)")
            c.execute("INSERT INTO wallet VALUES (:date, :category, :amount)",
                      {
                        'date': time.strftime("%c"),
                        'category': drop.get(),
                        'amount': sumbox.get()
                          })
            conn.commit()
            conn.close()
            sumbox.delete(0, END)
            drop.delete(0, END)
            
        def add_income():
            conn = sqlite3.connect('Money.db')
            c = conn.cursor()
            c.execute("INSERT INTO income VALUES (:date, :category, :amount)",
                      {
                        'date': time.strftime("%c"),
                        'category': drop2.get(),
                        'amount': sumbox2.get()
                          })
            conn.commit()
            conn.close()
            sumbox2.delete(0, END)
            drop2.delete(0, END)
            
        def query(): #just to check it's working
            conn = sqlite3.connect('Money.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM wallet")
            records = c.fetchall()
            print(records)
            conn.commit()
            conn.close()
            
            #Spendings
        sp_label = Label(self, text="Spendings")
        sp_label.grid(row=0, column=0)
        cat_label = Label(self, text="Choose category: ")
        cat_label.grid(row=1, column=0)        
        sum_label = Label(self, text="Amount: ")
        sum_label.grid(row=1, column=0)        
        drop = ttk.Combobox(self, value=['...', 'Rent', 'Travel','Groceries', 'Subscription', 'Guilty Pleasures'])
        drop.current(0)
        drop.grid(row=1, column=1)       
        sumbox = Entry(self, width=40, bd=3)
        sumbox.grid(row=2, column=1)        
        addB = ttk.Button(self, text = "add", command = add_transaction)
        addB.grid(row=3, column=0)
        query_btn = ttk.Button(self, text="show records", command = query)
        query_btn.grid(row= 4, column=0)    
            #Income
        in_label = Label(self, text="Income")
        in_label.grid(row=0, column=2)
        cat_label2 = Label(self, text="Choose category: ")
        cat_label2.grid(row=1, column=2)
        sum_label2 = Label(self, text="Amount: ")
        sum_label2.grid(row=2, column=2)
        drop2 = ttk.Combobox(self, value=['...', 'Salary', 'Debts', 'Sudden income', 'Other'])
        drop2.current(0)
        drop2.grid(row=1, column=3)
        sumbox2 = Entry(self, width=40, bd=3)
        sumbox2.grid(row=2, column=3) 
        addBin = ttk.Button(self, text = "add", command = add_income)
        addBin.grid(row=3, column=2)
        
        conn.commit()
        conn.close()
                
# fourth window for creating new account

class CNA(tk.Frame): 

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Create New Account")

        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Main Window",
                            command = lambda : controller.show_frame(MainWindow))
        # putting the button in its place by 
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Back to Log in page",
                            command = lambda : controller.show_frame(Log_in_Page))    
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
# fifth frame for editing account
  
class Edit_Account(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        RandomLabel = Label(self, text="idk")
        RandomLabel.grid(row=0, column=0)

# sixth for set up
        
class SetUp_Page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)

# seven, Summary
        
class Summary_Page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
    

app = AlfaApp()
app.mainloop()
