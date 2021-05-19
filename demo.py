

# f = open("savings.txt", 'r')
# filedata = f.read()
# print(filedata.splitlines())

# f.close()

# newdata = filedata.replace("saving", "newdata")


# f = open("savings.txt", 'w')
# f.write(newdata)
# f.close()
# x = []
# y = []
# for line in open("savings.txt", "r").readlines():  # Read the lines
#     # Split on the space, and store the results in a list of two strings
#     info = line.split()
#     x.append(info[0])
#     y.append(info[1])


# f = open("savings.txt", 'w')
# open("savings.txt", 'w').close()

# f.write("saving "+str(100))
# f.write("\n")
# f.write("target "+str(300))

# f.close()
# print(y)


# import tkinter as tk
# import pandas as pd
# import sqlite3
# from pandastable import Table, TableModel


# def select_all():
#     conn = sqlite3.connect('Money_Transaction.db')

#     df = pd.read_sql("Select * from wallet", conn)
#     conn.commit()
#     return df


# root = tk.Tk()
# root.geometry("660x600")

# frame_table = tk.Frame(root)
# frame_table.pack()
# pt = Table(frame_table)
# pt.updateModel((TableModel(select_all())))
# pt.show()
# root.mainloop()


# import tkinter as tk
# import requests
# import time


# def getWeather(canvas):
#     city = textField.get()
#     api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
#         "Finland"+"&appid=06c921750b9a82d8f5d1294e1586276f"

#     json_data = requests.get(api).json()
#     condition = json_data['weather'][0]['main']
#     temp = int(json_data['main']['temp'] - 273.15)

#     final_info = condition + " " + str(temp) + "°C"

#     label1.config(text=final_info)


# canvas = tk.Tk()
# canvas.geometry("600x500")
# canvas.title("Weather App")
# f = ("poppins", 15, "bold")
# t = ("poppins", 35, "bold")

# textField = tk.Entry(canvas, justify='center', width=20, font=t)
# textField.pack(pady=20)
# textField.focus()
# textField.bind('<Return>', getWeather)

# label1 = tk.Label(canvas, font=t)
# label1.pack()
# label2 = tk.Label(canvas, font=f)
# label2.pack()
# canvas.mainloop()
# import matplotlib.pyplot as plt
# import sqlite3
# import math
# import random
# import pandas as pd
# import tkinter as tk
# from matplotlib.pyplot import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# import matplotlib
# matplotlib.use('TkAgg')  # choose backend

# # --- other ---

# # --- for example data --

# # --- random data ---

# df1 = pd.DataFrame([random.randint(10, 100) for _ in range(3)])


# # --- GUI ---

# root = tk.Tk()

# # top frame for canvas and toolbar - which need `pack()` layout manager
# top = tk.Frame(root)
# top.pack()

# # bottom frame for other widgets - which may use other layout manager
# bottom = tk.Frame(root)
# bottom.pack()

# # --- canvas and toolbar in top ---

# # create figure
# fig = matplotlib.pyplot.Figure()

# # create matplotlib canvas using `fig` and assign to widget `top`
# canvas = FigureCanvasTkAgg(fig, top)

# # get canvas as tkinter widget and put in widget `top`
# canvas.get_tk_widget().pack()

# # create toolbar
# # toolbar = NavigationToolbar2Tk(canvas, top)
# # toolbar.update()
# # canvas._tkcanvas.pack()

# # --- first plot ---

# # create first place for plot

# date = '4'
# total_bal = 0

# conn = sqlite3.connect('Money_Transaction.db')

# c = conn.cursor()

# c.execute("select sum(amount) from wallet where substr(date,0,2) =(?) and CATEGORY='Rent' and TYPE=0 ", (date))
# records_rent = c.fetchall()
# if(not all(records_rent[0])):
#    # int value
#     total_bal_rent = 0

# else:
#     total_bal_rent = int(''.join(map(str, records_rent[0])))


# c.execute("select sum(amount) from wallet where substr(date,0,2) =(?) and CATEGORY='Travel' and TYPE=0", (date))
# records_travel = c.fetchall()

# if(not all(records_travel[0])):
#    # int value
#     total_bal_travel = 0

# else:
#     total_bal_travel = int(''.join(map(str, records_travel[0])))


# c.execute("select sum(amount) from wallet where substr(date,0,2) =(?) and CATEGORY='Grocereis' and TYPE=0", (date))
# records_groc = c.fetchall()

# if(not all(records_groc[0])):
#    # int value
#     total_bal_groc = 0

# else:
#     total_bal_groc = int(''.join(map(str, records_groc[0])))


# c.execute("select sum(amount) from wallet where substr(date,0,2) =(?) and CATEGORY='Subscription' and TYPE=0", (date))
# records_subs = c.fetchall()

# if(not all(records_subs[0])):
#    # int value
#     total_bal_subs = 0

# else:
#     total_bal_subs = int(''.join(map(str, records_subs[0])))


# c.execute("select sum(amount) from wallet where substr(date,0,2) =(?) and CATEGORY='Guilty Pleasure'and TYPE=0", (date))
# records_guilty = c.fetchall()

# if(not all(records_guilty[0])):
#    # int value
#     total_bal_guilty = 0

# else:
#     total_bal_guilty = int(''.join(map(str, records_guilty[0])))


# ax1 = fig.add_subplot(111)
# df = pd.DataFrame({'Catagories': ['Rent', 'Travel', 'Grocereis',
#                                   'Subscription', 'Guilty Pleasure'], 'Spendings': [total_bal_rent, total_bal_travel, total_bal_groc, total_bal_subs, total_bal_guilty]})
# df.plot.bar(x='Catagories', y='Spendings', rot=0, ax=ax1)

# root.mainloop()


# df1.plot(kind='bar', legend=True, ax=ax1)


# # --- second plot ---

# # create second place for plot
# ax2 = fig.add_subplot(212)

# # draw on this plot
# df2.plot(kind='bar', legend=False, ax=ax2)

# # --- other widgets in bottom ---

# b = tk.Button(bottom, text='Exit', command=root.destroy)
# b.pack()

# --- start ----


# creating the dataset
# data = {'C':20, 'C++':15, 'Java':30,
#         'Python':35}
# courses = list(data.keys())
# values = list(data.values())

# fig = plt.figure(figsize = (10, 5))

# # creating the bar plot
# plt.bar(courses, values, color ='maroon',
#         width = 0.4)

# plt.xlabel("Courses offered")
# plt.ylabel("No. of students enrolled")
# plt.title("Students enrolled in different courses")
# plt.show()


# Python Program to make a scrollable frame
# using Tkinter

from tkinter import *


class ScrollBar:

    # constructor
    def __init__(self):

        # create root window
        root = Tk()

        # create a horizontal scrollbar by
        # setting orient to horizontal
        h = Scrollbar(root, orient='horizontal')

        # attach Scrollbar to root window at
        # the bootom
        h.pack(side=BOTTOM, fill=X)

        # create a vertical scrollbar-no need
        # to write orient as it is by
        # default vertical
        v = Scrollbar(root)

        # attach Scrollbar to root window on
        # the side
        v.pack(side=RIGHT, fill=Y)

        # create a Text widget with 15 chars
        # width and 15 lines height
        # here xscrollcomannd is used to attach Text
        # widget to the horizontal scrollbar
        # here yscrollcomannd is used to attach Text
        # widget to the vertical scrollbar
        t = Text(root, width=15, height=15, wrap=NONE,
                 xscrollcommand=h.set,
                 yscrollcommand=v.set)

        # insert some text into the text widget
        for i in range(20):
            t.insert(END, "this is some text\n")

        # attach Text widget to root window at top
        t.pack(side=TOP, fill=X)

        # here command represents the method to
        # be executed xview is executed on
        # object 't' Here t may represent any
        # widget
        h.config(command=t.xview)

        # here command represents the method to
        # be executed yview is executed on
        # object 't' Here t may represent any
        # widget
        v.config(command=t.yview)

        # the root window handles the mouse
        # click event
        root.mainloop()


# create an object to Scrollbar class
s = ScrollBar()
