from tkinter import *
from tkinter import messagebox
import pyperclip

from classes.password_generator import PasswordGenerator

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    input_password.delete(0, END)
    generated_password = PasswordGenerator()
    password = generated_password.generate()
    input_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    is_ok = False

    if input_website.get() == "" or input_email.get() == "" or input_password.get() == "":
        messagebox.showinfo("Missing input", "Please, insert data in all fields")
        return
    password = f"{input_website.get()} | {input_email.get()} | {input_password.get()} \n"

    is_ok = messagebox.askokcancel(title="Save password", message="Are you sure you want to save?")

    if is_ok:
        with open("saved_passwords/passwords.txt", mode="a") as file:
            file.writelines(password)
            input_website.delete(0, END)
            input_password.delete(0, END)
        print("Saved!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_image = PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=1)

# website
label_website = Label(text="Website:", bg="white")
label_website.grid(column=0, row=2)
input_website = Entry(width=35)
input_website.focus()
input_website.grid(column=1, row=2, columnspan=2, sticky="ew")

# email/username
label_email= Label(text="Email/Username:", bg="white")
label_email.grid(column=0, row=3)
input_email = Entry(width=35)
input_email.insert(0, "email@gmail.com")
input_email.grid(column=1, row=3, columnspan=2, sticky="ew")

# password
label_password = Label(text="Password:", bg="white")
label_password.grid(column=0, row=4, sticky="ew")
input_password = Entry(width=21)
input_password.grid(column=1, row=4, sticky="ew")

# save
button_password = Button(text="Generate", bg="white", command=gen_pass)
button_password.grid(column=2, row=4, sticky="ew")

button_save = Button(text="Add", bg="white", width=36, command=save_password)
button_save.grid(column=1, row=5, columnspan=2, sticky="ew")

window.mainloop()