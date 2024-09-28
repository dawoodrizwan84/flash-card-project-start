from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def words_choice():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_img, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_img, image=back_image)

def is_known():
   to_learn.remove(current_card)
   data = pd.DataFrame(to_learn)
   data.to_csv("data/words_to_learn.csv", index=False)
   print(len(to_learn))
   words_choice()


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)



back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan = 2)


cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=words_choice)
cross_button.grid(row=1, column=0,)

checked_img = PhotoImage(file="images/right.png")
check_button = Button(image=checked_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)



words_choice()


window.mainloop()