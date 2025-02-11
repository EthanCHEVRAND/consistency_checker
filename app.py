from tkinter import *
from tkinter import ttk
from time import time_ns

last_click = time_ns()

"""
This function records when a click happens, updates the last_click global variable and calls the show_time function
Parameters : 
    event -> event sent by tkinter
"""
def key_press(event):
    global last_click
    current_click = time_ns()
    time = current_click - last_click
    last_click = current_click
    show_time(time)


"""
This function is used to calculate the delta between tow consecutive clicks and displays it in a terminal + in the tkinter window
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
    result.config(text=(time, unit))
    print(time, unit)


root = Tk()

root.geometry('640x480')
result=Label(root, height=5, width=20, text="cliquez")
result.pack()
root.bind('<Key>', key_press)

mainloop()