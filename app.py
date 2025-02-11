from tkinter import *
from time import time_ns

last_click = time_ns()
print(last_click)

def key_press(event):
    global last_click
    current_click = time_ns()
    time = current_click - last_click
    last_click = current_click
    show_time(time)

def show_time(time):
    unit = "ms"
    time /= 1000000
    if time >= 1000:
        unit = "s"
        time /= 1000
    print(time, unit)


root = Tk()
root.geometry('640x480')
root.bind('<Key>', key_press)
mainloop()