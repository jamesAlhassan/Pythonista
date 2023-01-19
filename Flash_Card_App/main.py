from tkinter import *

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"


# Window Setup
window = Tk()
window.title('Flashy')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Canvas Setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=front_img)
canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
canvas.create_text(400, 263, text='Word', font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons Setup
cross_img = PhotoImage(file='./images/wrong.png')
cross_button = Button(image=cross_img, highlightthickness=0)
cross_button.grid(row=1, column=0)

check_img = PhotoImage(file='./images/right.png')
check_button = Button(image=check_img, highlightthickness=0)
check_button.grid(row=1, column=1)





window.mainloop()