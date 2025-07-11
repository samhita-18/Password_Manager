from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json
FONT = ("Arial", 10, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols +password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any filed empty.")

    else:
        try:
            with open("data.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0,END)
            password_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lock_img)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1,row=1)

email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2,columnspan=2)
email_input.insert(0, "qwerty@gmail.com")


password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)


generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
        else:
            messagebox(title="Error", message=f"No details for {website} exists.")


search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, columnspan=2)




window.mainloop()

