from tkinter import *
from tkinter import messagebox
def setup_def():

    def writing():
        with open("default email.txt", "w") as file:
            file.write(entry.get())
            messagebox.showinfo(title="Completed", message="Changes will be applied when"
                                                           "program get restarted")
    window3 = Tk()
    window3.config(padx=20, pady=20)
    window3.title("Setup")
    window3.resizable(False, False)

    label = Label(window3, text="Type here default email/username\n that you want: ")
    label.grid(column=0, row=0)

    entry = Entry(window3, width=20)
    entry.grid(column=1, row=0)

    button = Button(window3, text="Change", width=40, command=writing)
    button.grid(column=0, row=1, columnspan=2)