from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
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
    if len(website_input.get())== 0 or  len(pass_input.get()) == 0:
        messagebox.showinfo(title = "Oops" , message = "Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title = website_input.get() , message=f"These are the details entered: \n Email : {email_input.get()}"
                                                               f"\n Password : {pass_input.get()} "                                                  f"\n Is it okay to save? ")
        if is_ok:
            with open("data.txt" ,"a") as file:
                file.write(f"{website_input.get()} | {email_input.get()} | {pass_input.get()} \n" )
                website_input.delete(0,END)
                pass_input.delete(0,END)
                website_input.focus()



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
website_input = Entry(width = 56)
website_input.focus()
website_input.grid(column = 1 , row = 1 , columnspan = 2)
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






window.mainloop()
