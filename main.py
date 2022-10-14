from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
import pyperclip
from all_passwords import window_with_passwords
import json
from setup_default import setup_def

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    password = password_generator()
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }}
    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username}\n"
                                                              f"Password: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- DEFAULT PASSWORD ------------------------------- #
with open("default email.txt") as file:
    default_email = file.readline()

# ---------------------------- SEARCH BUTTON ------------------------------- #
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        try:
            details = data[website]
        except KeyError:
            messagebox.showerror(title="Error", message="No details for the website exists")
        else:
            email = details["email"]
            password = details["password"]
            messagebox.showinfo(title=website, message=f"Email/username: {email}\n"
                                                       f"Password: {password}")

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=12)
window.resizable(False, False)

# Picture
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=2)

# Labels
website_label = Label(text="Website")
website_label.grid(column=0, row=3)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=4)

password_label = Label(text="Password:")
password_label.grid(column=0, row=5)

# Entries
website_entry = Entry()
website_entry.config(width=35)
website_entry.grid(column=1, row=3, columnspan=2)
website_entry.focus()

email_username_entry = Entry()
email_username_entry.config(width=35)
email_username_entry.grid(column=1, row=4, columnspan=2)
email_username_entry.insert(0, default_email)

password_entry = Entry()
password_entry.config(width=26)
password_entry.grid(column=1, row=5)

# Buttons
# password_settings_button = Button(text="Password settings")
# password_settings_button.grid(column=2, row=0)

setup_default_button = Button(text="Setup default\nemail/username", command=setup_def)
setup_default_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=5)
generate_password_button.config(padx=0, pady=0)

add_button = Button(text="Add", width=31, command=add_password)
add_button.grid(column=1, row=6, columnspan=2)

show_all_passwords_button = Button(text="Show all passwords", width=31, command=window_with_passwords)
show_all_passwords_button.grid(column=1, row=7, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=3)


window.mainloop()