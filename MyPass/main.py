from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('My Password Manager')
window.config(padx=20, pady=20, bg='white')


canvas = Canvas(width=400, height=380, bg='white', highlightthickness=0)
canvas_img = PhotoImage(file='logo.png')
canvas.create_image(200, 180, image=canvas_img)
canvas.grid()



window.mainloop()