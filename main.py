# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 12:18:30 2021

@author: mohse
"""

import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import * #need to install in your laptop

root = Tk()
root.geometry("700x500")
root.title('ALFA TEAM')

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
            open_mainwindow()
        else:
            messagebox.showerror(title="Error", message="Wrong Password")
    else:
        messagebox.showerror(title="Error", message="No user found")
        
  # open new Window and destroy previous ONE.


def show_frame(frame):
    frame.tkraise()


def open_mainwindow():
    global clockBtn
    root.destroy()
        
    mainWindow = Tk()
    mainWindow.geometry("950x500")
    mainWindow.title('welcom to Alfa App ')
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
    
      # Frames
    frame_add = Frame(mainWindow, width=280, height=480,
                      )

    frame_add.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
    frame_add.grid_propagate(False)
    
    frame_middle_1 = Frame(mainWindow, width=590, height=480,
                           )
    frame_middle_2 = Frame(mainWindow, width=590, height=480,
                           )
    frame_middle_3 = Frame(mainWindow, width=590, height=480,
                           )

    for frame in (frame_middle_1, frame_middle_2, frame_middle_3):
        frame.grid(row=0, column=1, padx=10, pady=10, sticky='nw')
        frame.grid_propagate(False)

    show_frame(frame_middle_1)



    # Buttons
    logoutBtn = Button(frame_middle_1, text="Logout", bg="#4465f9",
                       fg="white", height=1, width=15, font="Raleway", command=mainWindow.quit)
    logoutBtn.grid(row=0, column=2, pady=20, padx=120)

    transacBtn = Button(frame_middle_1, text="Add Transaction", bg="#4465f9",
                        fg="white", height=1, width=15, font="Raleway", command=lambda: show_frame(frame_middle_2))
    transacBtn.grid(row=1, column=2, pady=20, padx=120)

    editBtn = Button(frame_middle_1, text="Edit account", bg="#4465f9",
                     fg="white", height=1, width=15, font="Raleway")
    editBtn.grid(row=2, column=2, pady=20, padx=120)

    setupBtn = Button(frame_middle_1, text="Setup", bg="#4465f9",
                      fg="white", height=1, width=15, font="Raleway")
    setupBtn.grid(row=3, column=2, pady=20, padx=120)

    summaryBtn = Button(frame_middle_1, text="Account Summary", bg="#4465f9",
                        fg="white", height=1, width=15, font="Raleway")
    summaryBtn.grid(row=4, column=2, pady=20, padx=120)
    playBtn = Button(frame_middle_1, text="Play Lotto", bg="#4465f9",
                     fg="white", height=1, width=15, font="Raleway")
    playBtn.grid(row=5, column=2, pady=20, padx=120)

    clockBtn = PhotoImage(file='images/clockv2.png')

    getTimeBtn = Button(frame_add, image=clockBtn, border=0,
                        command=time)

    getTimeBtn.grid(row=0, column=0, pady=20, padx=5, sticky="ew")

     # Time Label
    global time_label
    time_label = Label(frame_add, text="Pick Time", font=("Arial", 10))
    time_label.grid(row=1, column=0, pady=5, padx=20,)

    # Calender

   # cal = Calendar(frame_add, selectmode="day", year=2021,
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
