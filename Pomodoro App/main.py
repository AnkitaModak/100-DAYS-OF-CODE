from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text = "TIMER")
    canvas.itemconfig(timer_text, text = "00.00")
    tick_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global timer_label
    global reps
    reps+= 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="BREAK", fg=RED)

    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="BREAK", fg=PINK)

    else:
        countdown(work_sec)
        timer_label.config(text="WORK", fg=GREEN, bg=YELLOW)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    global tick_label
    count_min = math.floor(count / 60)
    count_sec= count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min} : {count_sec}")
    if count > 0 :
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range (math.floor(reps / 2)):
            marks += "✔️"
        tick_label.config(text = marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100 , pady = 50, bg = YELLOW)

canvas = Canvas(width=200 , height = 233 ,  bg = YELLOW , highlightthickness= 0)
tomato_image = PhotoImage(file = "tomato.png")
canvas.create_image(100,115, image = tomato_image)
timer_text = canvas.create_text(100,130,text = "00.00", fill = "white" , font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1 , column = 1)

timer_label = Label(text= "TIMER" , fg = GREEN , bg = YELLOW , font=(FONT_NAME , 20 , "bold"))
timer_label.grid(row = 0 , column = 1)

tick_label = Label(fg = GREEN , bg = YELLOW , font=(FONT_NAME , 20 , "bold"))
tick_label.grid(row=3, column=1)

start_button = Button(text="Start" , command= start_timer )
start_button.grid(row= 2 , column = 0)

reset_button = Button(text="Reset" , command = reset_timer)
reset_button.grid(row= 2 , column = 2)

window.mainloop()







