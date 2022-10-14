from tkinter import *
import json
def window_with_passwords():


    window2 = Tk()
    window2.config(padx=20, pady=20)
    window2.title("All passwords")
    window2.resizable(False, False)

    website_label2 = Label(window2, text="Website")
    website_label2.grid(column=0, row=0)

    email_username_label2 = Label(window2, text="Email/Username")
    email_username_label2.grid(column=1, row=0)

    password_label2 = Label(window2, text="Password")
    password_label2.grid(column=2, row=0)

    with open("data.json") as data_file:
        all_passwords = json.load(data_file)
        keys = list(all_passwords.keys())
        for num in range(len(all_passwords)):
            details = all_passwords[keys[num]]

            website = keys[num]
            website_name = Label(window2, text=website)
            website_name.grid(column=0, row=num+1)

            email = details["email"]
            email_name = Label(window2, text=email)
            email_name.grid(column=1, row=num+1)

            password = details["password"]
            password_name = Entry(window2, width=25)
            password_name.insert(0, password)
            password_name.grid(column=2, row=num+1)

