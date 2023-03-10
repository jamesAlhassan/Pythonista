import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
# COLOURS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# OTHER
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 15
LONG_BREAK_MIN = 90
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text='Timer')
    check_mark.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    global reps
    reps = 0
# ---------------------------- START TIMER------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        counter(LONG_BREAK_MIN)
        timer_label.config(text='BREAK', fg=RED)
    elif reps % 2 == 0:
        counter(SHORT_BREAK_MIN)
        timer_label.config(text='REST', fg=PINK)
    else:
        counter(WORK_MIN)
        timer_label.config(text='WORKOUT...', fg=GREEN)


# ---------------------------- COUNTDOWN ------------------------------- #


def counter(count):
    if count < 10:
        canvas.itemconfig(timer_text, text=f'00:0{count}')
    else:
        canvas.itemconfig(timer_text, text=f'00:{count}')

    if count > 0:
        global timer
        timer = window.after(1000, counter, count - 1)
    else:
        start_timer()
        checks = ''
        sessions = math.floor(reps/2)
        for session in range(sessions):
            checks += '✅'
            check_mark.config(text=f'{checks} exercise(s) completed')






# ---------------------------- UI SETUP ------------------------------- #

# Window/Screen Setup


window = Tk()
window.title('Workout Timer')
window.config(padx=100, pady=50, bg=YELLOW)


# Labels
timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'italic'))
timer_label.grid(column=1, row=0)

# Canvas Setup
canvas = Canvas(width=300, height=307, bg=YELLOW, highlightthickness=0)
canvas_img = PhotoImage(file='workout-removebg-preview.png')
canvas.create_image(150, 175, image=canvas_img)
timer_text = canvas.create_text(160, 30, text='00:00', fill=RED, font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


# Buttons
start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

# Check Mark
check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, 'bold'))
check_mark.grid(column=1, row=3)


window.mainloop()