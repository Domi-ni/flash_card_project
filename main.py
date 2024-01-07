from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- DATA SETTINGS ------------------------------- #

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = random.choice(to_learn)

# ---------------------------- CARD MECHANISM ------------------------------- #


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card, image=front_card_img)
    canvas.itemconfig(card_title, text="French", fill="white")
    canvas.itemconfig(card_word, text=current_card["French"], fill="white")


def flip_card():
    canvas.itemconfig(card, image=back_card_img)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 265, image=front_card_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 30, "italic"), fill="white")
card_word = canvas.create_text(400, 260, text="word", font=("Ariel", 50, "bold"), fill="white")
canvas.grid(row=0, column=0, columnspan=3)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

show_card_img = PhotoImage(file="images/show_card.png")
show_card_button = Button(image=show_card_img, highlightthickness=0, command=flip_card)
show_card_button.grid(row=1, column=1)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=2)

next_card()
window.mainloop()