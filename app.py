from tkinter import *
from tkinter import ttk
from time import time_ns

# -------------------------------------------------- global variables --------------------------------------------------

last_click = time_ns()
last_time = 1
accuracy = "100%"


# -------------------------------------------------- functions --------------------------------------------------

"""
This function records when a click happens, updates the last_click global variable and calls the show_time function
Parameters : 
    event -> event sent by tkinter
"""
def key_press(event):
    global last_click
    global last_time
    current_click = time_ns()
    time = current_click - last_click
    
    calc_accuracy(time)
    show_time(time)

    last_time = time
    last_click = current_click


"""
This function is used to calculate the delta between tow consecutive clicks and displays it in the tkinter window
Parameters : 
    time -> the time.time_ns() of the current click 
"""
def show_time(time):
    unit = "ms"
    time /= 1000000
    if time >= 1000:
        unit = "s"
        time /= 1000
    time=round(time, 2)
    result_acc.config(text=(time, unit))


"""
This function is used to calculate the accuracy of a click depending on the previous click, and displays it in the tkinter window
Parameters : 
    time -> the time.time_ns() of the current click 
"""
def calc_accuracy(time):
    global accuracy
    acc = 100 * (time / last_time)
    if acc > 100:
        acc = 200 - acc
    if acc < 0:
        acc = 0
    accuracy = str(round(acc, 2))
    accuracy += "%"
    accur.config(text=accuracy)


def show_acc():
    spdtest.pack_forget()
    acctest.pack(fill="both", expand=True)

def show_spd():
    acctest.pack_forget()
    spdtest.pack(fill="both", expand=True)

# -------------------------------------------------- tkinter ---------------------------------------------------

root = Tk()
root.geometry('640x480')

nav = Frame(root, height=50)
nav.pack(fill="x")
nav_spdtest = Button(nav, text="speedtest", command=show_acc)
nav_spdtest.pack()
nav_acctest = Button(nav, text="accuracy test", command=show_acc)
nav_acctest.pack()

acctest = Frame(root)
result_acc=Label(acctest, height=5, width=20, text="cliquez")
result_acc.pack()
accur=Label(acctest, height=5, width=20, text="")
accur.pack()

spdtest = Frame(root)
result_spd=Label(spdtest, height=5, width=20, text="cliquez (10 sec)")
result_spd.pack()

show_acc()

root.bind('<Key>', key_press)

mainloop()