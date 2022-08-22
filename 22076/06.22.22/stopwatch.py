from tkinter import *
root = Tk()
root.title("Stopwatch")
root.config(bg="black")
width = 500
height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))

milisec=00
sec=00
min=00
def Start():
    global time, timer, milisec, sec, min
    milisec += 1
    if milisec==100:
        milisec=0
        sec=sec+1
    if sec==60:
        sec=0
        min=min+1
    timer.config(text=f'{min}:{sec}:{milisec}')
    time = timer.after(200, Start)

def Stop():
    global time
    timer.after_cancel(time)

def Reset():
    global milisec, sec, min
    milisec = 00
    sec = 00
    min = 00
    timer.config(text=f'{min}:{sec}:{milisec}')
    timer.after_cancel(time)

def Exit():
    root.destroy()


Top = Frame(root, width=400, bg="green2")
Top.pack(side=TOP)
Bottom= Frame(root, width=400, bg="black")
Bottom.pack(side=BOTTOM)
Title = Label(Top, text="StopWatch", font="arial 24 bold",
              fg="gold", bg="black")
Title.pack(fill=X)
timer = Label(Top, font=("times new roman", 45), fg="white",
              bg="black")
timer.pack(fill=X, expand=NO, pady=10)
timer.config(text=f'{min}:{sec}:{milisec}')
Startt = Button(Bottom, text='START', font="arial 20 bold",
                fg="purple4", width=6, command=Start)
Startt.pack(side=LEFT, padx=2, pady=5)





Stopp = Button(Bottom, text='STOP', font="arial 20 bold",
               fg="red", width=6, command=Stop)
Stopp.pack(side=LEFT, padx=2, pady=5)





Resett = Button(Bottom, text='RESET', font="arial 20 bold",
                fg="purple4", width=6, command=Reset)
Resett.pack(side=LEFT, padx=2, pady=5)
Exitt = Button(Bottom, text='CLOSE', font="arial 20 bold",
               fg="red", width=6, command=Exit)
Exitt.pack(side=LEFT, padx=2, pady=5)

root.mainloop()
