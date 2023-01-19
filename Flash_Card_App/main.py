from tkinter import *
import pandas as pd
from random import choice

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"

# data
data = pd.read_csv('./data/french_words.csv')
data_dict = data.to_dict(orient='records')
to_learn = choice(data_dict)
print(to_learn['French'])


# Functions
def next_word():
    to_learn = choice(data_dict)
    canvas.itemconfig(language, text='French')
    canvas.itemconfig(word, text=to_learn['French'])


# Window Setup
window = Tk()
window.title('Flashy')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Canvas Setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=front_img)
language = canvas.create_text(400, 150, text='Language', font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text='Word', font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons Setup
cross_img = PhotoImage(file='./images/wrong.png')
cross_button = Button(image=cross_img, highlightthickness=0)
cross_button.grid(row=1, column=0)

check_img = PhotoImage(file='./images/right.png')
check_button = Button(image=check_img, highlightthickness=0, command=next_word)
check_button.grid(row=1, column=1)





window.mainloop()