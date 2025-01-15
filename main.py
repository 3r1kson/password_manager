from tkinter import *
from tkinter import messagebox
import pyperclip
import json

from classes.password_generator import PasswordGenerator
# ---------------------------- PASSWORD SEARCH ---------------------------------- #
def search_pass():
    website = input_website.get()

    if input_website.get() == "":
        messagebox.showinfo("Missing input", "Please, insert a website to search")
    else:
        try:
            with open("saved_passwords/passwords.json", mode="r") as file:
                data = json.load(file)
                if website in data:
                    email = data[website]["email"]
                    password = data[website]["password"]
                    print(email, password)
                    messagebox.showinfo(website, f"Email: {email} \nPassword: {password}")
                else:
                    messagebox.showinfo("Error", "No website found")

        except FileNotFoundError:
            messagebox.showinfo("Missing file", "File not found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    input_password.delete(0, END)
    generated_password = PasswordGenerator()
    password = generated_password.generate()
    input_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():


    website = input_website.get()
    email = input_email.get()
    password = input_password.get()

    new_data = {
        website: {
            "email" : email,
            "password": password,
        }
    }

    if input_website.get() == "" or input_email.get() == "" or input_password.get() == "":
        messagebox.showinfo("Missing input", "Please, insert data in all fields")
    else :
        try:
            with open("saved_passwords/passwords.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("saved_passwords/passwords.json", mode="a") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            with open("saved_passwords/passwords.json", mode="w") as data_file:
                data.update(new_data)
                json.dump(data, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)

    # is_ok = False
    # password = f"{input_website.get()} | {input_email.get()} | {input_password.get()} \n"

    # is_ok = messagebox.askokcancel(title="Save password", message="Are you sure you want to save?")

    # if is_ok:
    #     with open("saved_passwords/passwords.txt", mode="a") as file:
    #         # file.writelines(password)
    #         input_website.delete(0, END)
    #         input_password.delete(0, END)
    #     print("Saved!")

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
input_website.grid(column=1, row=2, sticky="ew")
button_password = Button(text="Search", bg="white", command=search_pass)
button_password.grid(column=2, row=2, sticky="ew")

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