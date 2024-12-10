import json
from json import JSONDecodeError
from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters =[choice(letters) for _ in range(randint(8, 10))]
    password_symbols =[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers =[choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global website_input
    global email_input
    global pass_input
    new_data = {website_input.get():{
        "email": email_input.get(),
        "password":pass_input.get(),
    }

                }
    if len(website_input.get())== 0 or  len(pass_input.get()) == 0:
        messagebox.showinfo(title = "Oops" , message = "Please don't leave any fields empty!")
    else:
        try:
            with open("data.json" ,"r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError,UnboundLocalError,JSONDecodeError):
            data = new_data
            with open("data.json", "w") as data_file:
                json.dump(data , data_file , indent = 4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0,END)
            pass_input.delete(0,END)
            website_input.focus()
def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        if website_input.get() in data:
            email = data[website_input.get()]["email"]
            password = data[website_input.get()]["password"]
            messagebox.showinfo(title = website_input.get() ,message= f"Email : {email}\nPassword : {password}" )
    except FileNotFoundError:
        messagebox.showerror(title="error" , message= "No data file found.")
    if len(website_input.get()) == 0:
        messagebox.showerror(title="error", message="It doesn't contain any information!")
    elif website_input.get() not in data:
        messagebox.showerror(title="error", message="No data file found.")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 20 , pady = 20)
canvas = Canvas(height = 200 , width = 200)
pass_image = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = pass_image)
canvas.grid(column =1 , row = 0)

website_label = Label(text = "Website:")
website_label.grid(column = 0 , row = 1)
website_input = Entry(width = 37)
website_input.focus()
website_input.grid(column = 1 , row = 1 )
email_label = Label(text = "Email/Username:")
email_label.grid(column = 0 ,row = 2)
email_input = Entry(width = 56)
email_input.insert(0,"ankita@gmail.com")
email_input.grid(column = 1 , row = 2 , columnspan = 2)
pass_label = Label(text = "Password:")
pass_label.grid(column = 0 , row= 3)
pass_input = Entry(width= 37 )
pass_input.grid(column = 1 , row = 3)
pass_button = Button(text= "Generate Password" ,  command = password_generator)
pass_button.grid(column = 2 , row = 3)
add_button = Button(text= "Add" , width = 47 ,command= save)
add_button.grid(column = 1 ,row = 4 , columnspan = 2)
search_button = Button(text= "Search" ,width=14 ,command=find_password )
search_button.grid(column = 2 , row = 1)





window.mainloop()

