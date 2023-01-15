from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# Window/Screen Setup
window = Tk()
window.title('Workout Timer')
window.config(padx=100, pady=50, bg=YELLOW)


# Labels
timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'italic'))
timer_label.grid(column=1, row=0)

# Canvas Setup
canvas = Canvas(width=300, height=307, bg=YELLOW, highlightthickness=0)
canvas_img = PhotoImage(file='work_out.png')
canvas.create_image(150, 153, image=canvas_img)
canvas.create_text(190, 50, text='00:00', fill=RED, font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Button



window.mainloop()





