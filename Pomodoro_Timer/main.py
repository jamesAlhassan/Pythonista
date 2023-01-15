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
window.title('Pomodoro Timer')
window.config(padx=100, pady=50)

# Canvas Setup
canvas = Canvas(width=200, height=224)
canvas_img = PhotoImage(file='tomato.png')
canvas.create_image(103, 112, image=canvas_img)
canvas.pack()



window.mainloop()





