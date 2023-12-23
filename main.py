from tkinter import *
from tkinter import messagebox
import pyperclip
import secrets

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter = [secrets.SystemRandom().choice(letters) for i in range(secrets.SystemRandom().randint(8, 10))]


    password_symbols = [secrets.SystemRandom().choice(symbols) for items in range(secrets.SystemRandom().randint(2, 4))]

    password_numbers = [secrets.SystemRandom().choice(numbers) for item in range(secrets.SystemRandom().randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letter
    secrets.SystemRandom().shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def collection():

    a = web_input.get()
    b = e_input.get()
    c = password_input.get()

    if len(a) == 0:
        messagebox.showerror(title="Error", message="Please do not leave any fields empty!")
    elif len(c) == 0:
        messagebox.showerror(title="Error", message="Please do not leave any fields empty!")
    else:

        is_ok = messagebox.askokcancel(title=a, message=f"These are the details entered: \nEmail: {b} \nPassword: {c} \nIs it ok to save?")

        if is_ok:
            d = f"{a} | {b} | {c}\n"
            with open("data.txt", "a") as file:
                file.write(d)
            web_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
img_title = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_title)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

e_user_label = Label(text="Email/Username:")
e_user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

web_input = Entry(width=52)
web_input.focus()
web_input.grid(column=1, row=1, columnspan=2)

e_input = Entry(width=52)
e_input.insert(0, "user@email.com")
e_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=34)
password_input.grid(row=3, column=1)


generate_pass = Button(text="Generate Password", width=14, command=generate)
generate_pass.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=collection)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
