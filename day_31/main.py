import random
from tkinter import *
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = []
try:
    french_words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words = pd.read_csv("data/french_words.csv")
    to_learn = french_words.to_dict(orient="records")
else:
    to_learn = french_words.to_dict(orient="records")


def update_word():
    canvas.itemconfig(card_image, image=card_front_img)
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")


def update_words_to_learn():
    to_learn.remove(current_word)
    pf = pd.DataFrame(to_learn)
    pf.to_csv("data/words_to_learn.csv", index=False)
    update_word()



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "italic"))

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=update_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
unknown_button = Button(image=check_image, highlightthickness=0, command=update_words_to_learn)
unknown_button.grid(row=1, column=1)

update_word()

window.mainloop()
