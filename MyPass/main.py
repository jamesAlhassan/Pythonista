from tkinter import *
from tkinter import messagebox
import random as rd
import pyperclip
import json

COLOR = 'white'

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
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()

    new_data = {
        website_input: {
            'email': email_input, 'password': password_input
        }
    }

    if len(website_input) < 1 or len(password_input) < 1:
        messagebox.showerror(title='Error', message="Empty input!!!\nField can't be empty")
    else:
        is_ok = messagebox.askyesno(title=website_input,
                                    message=f'Confirm Your Details\n\nEmail: {email_input}\n\nPassword: '
                                            f'{password_input}\n\nDo you want to save?')
        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                # email_entry.delete(0, END)
                password_entry.delete(0, END)
        messagebox.showinfo(title='Done', message=f'{website_input} successfully added to the database')

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website_input = website_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
            try:
                website = data[website_input]
                email = website['email']
                password = website['password']
                messagebox.showinfo(title=website_input, message=f'Email: {email}\nPassword: {password}')
            except KeyError:
                messagebox.showinfo(title='Error', message=f'No Details found for {website_input}')
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('My Password Manager')
window.config(padx=100, pady=100, bg=COLOR)


canvas = Canvas(width=200, height=200, bg=COLOR, highlightthickness=0)
canvas_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=canvas_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:', bg=COLOR, pady=6)
website_label.grid(row=1, column=0)

email_label = Label(text='Email:', bg=COLOR, pady=6)
email_label.grid(row=2, column=0)

password_label = Label(text='Password:', bg=COLOR, pady=6)
password_label.grid(row=3, column=0)


# Entries
website_entry = Entry(width=27, bg=COLOR, highlightthickness=0)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=47, bg=COLOR, highlightthickness=0)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'example@abc.com')

password_entry = Entry(width=27, bg=COLOR, highlightthickness=0)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text='Generate Pass.', width=15, bg=COLOR, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=45, bg=COLOR, command=save_password_details)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text='Search', width=15, bg=COLOR, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
