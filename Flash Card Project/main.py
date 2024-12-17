from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
new_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("data/french_words.csv.csv")
    to_learn = og_data
else:
    to_learn = data.to_dict(orient = "records")

def card_generator():
    global flip_timer , new_card
    window.after_cancel(flip_timer)
    new_card = random.choice(to_learn)
    canvas.itemconfig(word_title , text =  new_card["French"] , fill = "black")
    canvas.itemconfig(card_title , text = "French" , fill = "black")
    canvas.itemconfig(card_bg, image = flash_card_front_image )
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global new_card
    new_card = random.choice(to_learn)
    canvas.itemconfig(card_title , text = "English" ,fill = "white" )
    canvas.itemconfig(word_title, text=new_card["English"] , fill = "white")
    canvas.itemconfig(card_bg , image = flash_card_back_image )

def is_known():
    to_learn.remove(new_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv" , index = False)
    card_generator()

window = Tk()
window.title("Flash Cards")
window.config(padx=50 , pady = 50 , bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width =800 , height=526)
flash_card_front_image = PhotoImage(file="images/card_front.png")
flash_card_back_image = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400,263,image = flash_card_front_image)
card_title = canvas.create_text(400,150 , text = "Title " ,font=("Ariel", 40 , "italic"))
word_title = canvas.create_text(400,263,text ="word" , font =("Ariel" , 60 , "bold"))
canvas.grid(row = 0  ,column = 0 , columnspan = 2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=card_generator)
wrong_button.grid(row = 2 , column = 0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image ,command=is_known)
right_button.grid(row = 2 , column = 1)

card_generator()

window.mainloop()
