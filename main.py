import json
from tkinter import *
from tkinter import messagebox
import random as r


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    # delete previous entry.
    e3.delete(0, END)
    # Clear clipboard.
    e3.clipboard_clear()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []
    pass_string = ""

    for i in range(1, 5 + 1):
        password.append(r.choice(letters))
    for j in range(1, 1 + 1):
        password.append(r.choice(symbols))
    for k in range(1, 2 + 1):
        password.append(r.choice(numbers))

    r.shuffle(password)  # shuffle list.

    for single_char in password:
        pass_string += single_char  # list to string.
    e3.insert(END, f"{pass_string}")
    # To copy to clipboard.
    e3.clipboard_append(f"{pass_string}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    if len(e1.get()) == 0 or len(e2.get()) == 0 or len(e3.get()) == 0:
        messagebox.showerror(title="Error", message="Enter appropriate information.\n "
                                                    "Fields should not be kept empty.")
    else:
        if len(e3.get()) < 6:
            messagebox.showerror(title="Error", message="Password must be of at least 6 characters.")
        else:
            website = e1.get()
            mail = e2.get()
            pass_word = e3.get()
            new_data = {
                website: {
                    "email": mail,
                    "pass": pass_word
                }
            }
            try:
                with open("Password.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("Password.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            else:
                data.update(new_data)
                with open("Password.json", mode="w") as file:
                    json.dump(data, file, indent=4, separators=(",", ": "))
                    # Delete previous
                    e1.delete(0, END)
                    e2.delete(0, END)
                    e3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Search Password:
def find_pass():
    try:
        with open("Password.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title=FileNotFoundError, message="File Not found.")
    else:
        if e1.get() in data:
            uid = data[e1.get()]["email"]
            password = data[e1.get()]["pass"]
            messagebox.showinfo(title=e1.get(), message=f"G-mail/UserId: {uid}\npassword: {password}")
        else:
            if len(e1.get()) > 0:
                messagebox.showinfo(title="Error", message=f"No details of {e1.get()} found.")


# ---------------------------- UI SETUP ------------------------------- #
# Window:
window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

# Canvas:
canvas = Canvas(width=200, height=189, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=img)
canvas.grid(row=0, column=2)

# Labels:
l1 = Label(text="Website Link")
l1.grid(row=2, column=1)
l2 = Label(text="G-mail/User name")
l2.grid(row=3, column=1)
l3 = Label(text="Password")
l3.grid(row=4, column=1)

# Entry:
e1 = Entry()
e1.grid(row=2, column=2)
e2 = Entry()
e2.grid(row=3, column=2)
e3 = Entry()
e3.grid(row=4, column=2)

# Buttons:
b1 = Button(text="Generate Password", width=15, height=1, command=pass_generator)
b1.grid(row=4, column=3)
b2 = Button(text="Submit", command=save_pass)
b2.grid(row=5, column=2)
b3 = Button(text="Search", width=15, height=1, command=find_pass)
b3.grid(row=2, column=3)

window.mainloop()
