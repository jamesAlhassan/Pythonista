from tkinter import *
from tkinter import messagebox
import random as rd
import pyperclip
# ---------------------------- PASSWORD GENERATOR -------------------------------


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = []
    password_symbols = []
    password_numbers = []

    [password_letters.append(rd.choice(letters)) for _ in range(rd.randint(9, 10))]
    [password_symbols.append(rd.choice(symbols)) for _ in range(rd.randint(9, 10))]
    [password_numbers.append(rd.choice(numbers)) for _ in range(rd.randint(9, 10))]

    password_list = password_letters + password_numbers + password_symbols
    rd.shuffle(password_list)

    password = ''.join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password_details():
    num = 0
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    num += 1

    if len(website_input) < 1 or len(email_input) < 1 or len(password_input) < 1:
        messagebox.showerror(title='Error', message="Empty input!!!\nField can't be empty")
    else:
        is_ok = messagebox.askyesno(title=website_input,
                                    message=f'Details\nEmail: {email_input}\nPassword: '
                                            f'{password_input}\nDo you want to save?')
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f'SN: {num} | website: {website_input} | '
                           f'email: {email_input} | password: {password_input}\n')

                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('My Password Manager')
window.config(padx=100, pady=100, bg='white')


canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
canvas_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=canvas_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:', bg='white', pady=6)
website_label.grid(row=1, column=0)

email_label = Label(text='Email:', bg='white', pady=6)
email_label.grid(row=2, column=0)

password_label = Label(text='Password:', bg='white', pady=6)
password_label.grid(row=3, column=0)


# Entries
website_entry = Entry(width=45, bg='white', highlightthickness=0)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=45, bg='white', highlightthickness=0)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'example@abc.com')

password_entry = Entry(width=27, bg='white', highlightthickness=0)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text='Generate Pass.', width=15, bg='white', command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=45, bg='white', command=save_password_details)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
