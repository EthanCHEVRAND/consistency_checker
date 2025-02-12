# -------------------------------------------------- imports --------------------------------------------------

from tkinter import *
from tkinter import ttk
from time import time_ns, sleep


# -------------------------------------------------- global variables --------------------------------------------------

last_click = time_ns()
last_time = 1
accuracy = "100%"
best_accuracy = 0

click_count = 0
chrono = 10


# -------------------------------------------------- functions --------------------------------------------------

def init_acc():
    global last_click
    global last_time
    global accuracy
    global best_accuracy

    last_click = time_ns()
    last_time = 1
    accuracy = "100%"
    best_accuracy = 0

    result_acc.config(text="cliquez")
    accur.config(text="")

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
    global best_accuracy
    acc = 100 * (time / last_time)
    if acc > 100:
        acc = 200 - acc
    if acc < 0:
        acc = 0
    if acc > best_accuracy:
        best_accuracy = acc
        best_accur.config(text=(round(best_accuracy, 2), "%"))
    accuracy = str(round(acc, 2))
    accuracy += "%"
    accur.config(text=accuracy)

def start_spdtest_func():
    global chrono
    for i in range(chrono):
        sleep(1)
        chrono -= 1
    final_click_count = click_count
    spdtest_button.config(DISABLED)
    click_count_show.config(text=final_click_count)
        

def incr_spd():
    global click_count
    click_count += 1
    click_count_show.config(text=click_count)

def show_page(page):
    spdtest.pack_forget()
    acctest.pack_forget()
    reftest.pack_forget()

    if page == acctest:
        init_acc()

    page.pack(fill="both", expand=True)


# -------------------------------------------------- tkinter --------------------------------------------------

root = Tk()
root.geometry('640x480')

nav = Frame(root, height=50)
nav.pack(fill="x")
nav_spdtest = Button(nav, text="speedtest", command=lambda: show_page(spdtest))
nav_spdtest.pack(side="left")
nav_acctest = Button(nav, text="accuracy test", command=lambda: show_page(acctest))
nav_acctest.pack(side="left")
nav_reflextest = Button(nav, text="reflex test", command=lambda: show_page(reftest))
nav_reflextest.pack(side="left")

acctest = Frame(root)
result_acc=Label(acctest, width=20, text="click to start")
result_acc.pack()
accur=Label(acctest, width=20, text="")
accur.pack()
best_accur = Label(acctest, text=(best_accuracy, "%"))
best_accur.pack()

spdtest = Frame(root)
result_spd=Label(spdtest, height=5, width=20, text="")
result_spd.pack()
start_spdtest = Button(spdtest, text="start", command=start_spdtest_func)
start_spdtest.pack()
spdtest_button = Button(spdtest, height=10, width=30, text="click", command=incr_spd)
spdtest_button.pack()
click_count_show = Label(spdtest, text=click_count)
click_count_show.pack()

reftest = Frame(root)
result_ref=Label(reftest, height=5, width=20, text="cliquez (?)")
result_ref.pack()

show_page(acctest)

root.bind('<Key>', key_press)

mainloop()