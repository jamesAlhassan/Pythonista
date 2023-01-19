from tkinter import *
import pandas as pd
from random import choice
import time

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"

# data
data = pd.read_csv('./data/french_words.csv')
data_dict = data.to_dict(orient='records')
current_card = {}


# Functions
def timer(count):
    if count >= 0:
        timer_label.config(text=f'00:0{count}', bg='black', fg='white')
        window.after(1000, timer, count - 1)

def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    window.after_cancel(timer)
    current_card = choice(data_dict)
    canvas.itemconfig(language, text='French', fill='black')
    canvas.itemconfig(word, text=current_card['French'], fill='black')
    canvas.itemconfig(background, image=front_img)
    timer(5)
    flip_timer = window.after(5000, unknown_word)



def unknown_word():
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(word, text=current_card['English'], fill='white')
    canvas.itemconfig(background, image=back_img)



# Window Setup
window = Tk()
window.title('Flashy')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(5000, unknown_word)
# window.after(1000, timer)

# Canvas Setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
background = canvas.create_image(400, 263, image=front_img)

language = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=3)

# Buttons Setup
cross_img = PhotoImage(file='./images/wrong.png')
cross_button = Button(image=cross_img, highlightthickness=0, command=unknown_word)
cross_button.grid(row=1, column=0)

check_img = PhotoImage(file='./images/right.png')
check_button = Button(image=check_img, highlightthickness=0, command=next_word)
check_button.grid(row=1, column=2)

# timer
timer_label = Label(text='', font=('Helvetica', 40, 'bold'))
timer_label.grid(row=1, column=1)

next_word()
timer(5)
window.mainloop()