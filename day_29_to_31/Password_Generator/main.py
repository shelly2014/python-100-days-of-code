import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(letters) for _ in range(randint(2, 4))]
    password_list += [choice(letters) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, "end")
    password_entry.config(fg="black")
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Password", message="Password has been copied to clip board and is ready for use.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not check_input():
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                          f"\nPassword: {password} \nIs it ok to save?")

    if is_ok:
        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "r") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, "end")
            email_entry.delete(0, "end")
            password_entry.delete(0, "end")


# --------------------------- SEARCH PASSWORD -------------------------- #
def search_password():
    website = website_entry.get()
    if len(website) == 0 or website == website_entry_default:
        messagebox.showinfo(title="Oops", message="Please make sure the website is not empty.")
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found.")
    else:
        if website in data:
            messagebox.showinfo(title="Password Info",
                                message=f"{website}:\nUsername: {data[website]['email']}\n"
                                        f"Password: {data[website]['password']}\n"
                                        f"Password is copied and ready to paste")
            pyperclip.copy(data[website]['password'])
        else:
            messagebox.showinfo(title="Oops", message="No details for the website exists.")


# ---------------------------- HELP FUNCTION -------------------------- #
def clear_text(event):
    if event.widget.get() == website_entry_default or event.widget.get() == email_entry_default \
            or event.widget.get() == password_entry_default:
        event.widget.delete(0, "end")
        event.widget.config(fg="black")


def check_input():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0 or website == website_entry_default \
            or email == email_entry_default or password == password_entry_default:
        return False

    return True


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", fg="black", bg="white")
website_label.grid(column=0, row=1, stick="e")

website_entry = Entry(width=30, fg="grey")
website_entry_default = "Please enter website."
website_entry.insert(0, website_entry_default)
website_entry.bind("<FocusIn>", clear_text)
website_entry.grid(column=1, row=1, stick="w")

email_label = Label(text="Email/Username:", fg="black", bg="white")
email_label.grid(column=0, row=2, stick="e")

email_entry = Entry(width=50, fg="grey")
email_entry_default = "Please enter email or username."
email_entry.insert(0, email_entry_default)
email_entry.bind("<FocusIn>", clear_text)
email_entry.grid(column=1, columnspan=2, row=2, stick="w")

password_label = Label(text="Password:", fg="black", bg="white")
password_label.grid(column=0, row=3, stick="e")

password_entry = Entry(width=30, fg="grey")
password_entry_default = "Please enter/generate password."
password_entry.insert(0, password_entry_default)
password_entry.bind("<FocusIn>", clear_text)
password_entry.grid(column=1, row=3, stick="w")

gen_password_button = Button(borderwidth=1, highlightthickness=0, bg="white", command=gen_password,
                             text="Generate Password", fg="red", width=15)
gen_password_button.grid(column=2, row=3, stick="w")

add_button = Button(borderwidth=1, highlightthickness=0, bg="white", command=save_password,
                    text="Add", fg="red", width=43)
add_button.grid(column=1, columnspan=2, row=4, sticky="w")

search_password_button = Button(borderwidth=1, highlightthickness=0, bg="white", command=search_password,
                                text="Search", fg="red", width=15)
search_password_button.grid(column=2, row=1, stick="w")

window.mainloop()
