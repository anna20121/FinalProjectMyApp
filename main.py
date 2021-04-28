# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 12:18:30 2021

@author: mohse
"""

import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *

root = Tk()
root.geometry("700x500")
root.title('ALFA TEAM')

dpi = root.winfo_fpixels('1i')
print(f"Current dpi is set to {dpi}")

frame = Frame(root,)
# Labels tags

sign = Label(frame, text="Login", font=('Arial Bold', 18))
sign.grid(row=0, column=1, pady=(2, 20))

userLabel = Label(frame, text="Username: ")
userLabel.grid(
    row=1, column=0,)
PasswordLabel = Label(frame, text="Password: ")
PasswordLabel.grid(
    row=2, column=0, )


# Entry to the App
userName = Entry(frame, width=40, bd=3)
userName.grid(
    row=1, column=1, padx=15, pady=10)
Password = Entry(frame, width=35, show='*', bd=4)
Password.grid(
    row=2, column=1, padx=15, pady=10)


# functions needs to be here


def time():
    # current date and time

    now = datetime.now()
    date_time = now.strftime("%I:%M:%S")
    time_label.config(text=date_time)


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
            #open_mainwindow()
        else:
            messagebox.showerror(title="Error", message="Wrong Password")
    else:
        messagebox.showerror(title="Error", message="No user found")
        
    mainWindow = Tk()
    mainWindow.geometry("950x500")
    mainWindow.title('welcom to our App ')
    rootHeight = mainWindow.winfo_height()
    rootWidth = mainWindow.winfo_width()
    my_menu = Menu(mainWindow)
    mainWindow.config(menu=my_menu)

    # Menu
    # Files
    file_menu = Menu(my_menu)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save", command=mainWindow.quit)
    file_menu.add_command(label="Exit", command=mainWindow.quit)
    edit_menu = Menu(my_menu)
    my_menu.add_cascade(label="Edit", menu=edit_menu)

    option_menu = Menu(my_menu)
    my_menu.add_cascade(label="Options", menu=option_menu)

    Tools_menu = Menu(my_menu)
    my_menu.add_cascade(label="Tools", menu=Tools_menu)

    Help_menu = Menu(my_menu)
    my_menu.add_cascade(label="File", menu=Help_menu)
    
     # Time Label
    global time_label
    time_label = Label(frame_add, text="Pick Time", font=("Arial", 10))
    time_label.grid(row=1, column=0, pady=5, padx=20,)

    # Calender

    #cal = Calendar(frame_add, selectmode="day", year=2021,
                   #month=4, day=27, background="#4465f9",)
    cal.grid(row=2, column=0, pady=20, padx=20, )
    cal = calendar(winroot, font="Arial 8", 
                   locale="fi_FI", disabledforeground="red",
                   cursor="hand1")

# Buttons
loginBtn = Button(frame, text="login", bg="#4465f9",
                  fg="white", height=1, width=10, font="Raleway", command=verify_login)
loginBtn.grid(row=3, column=1, pady=5)


frame.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
