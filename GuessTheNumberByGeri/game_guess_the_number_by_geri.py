# Import Module
import tkinter as tk
from tkinter import *
import random


# define global variables:
number_to_guess = int()


def start_new_game():
    # Generate random number to be guessed
    global number_to_guess
    number_to_guess = random.randint(1, 100)
    game_canvas.itemconfig(response_to_player, text="")
    player_input.config(state=NORMAL)
    player_submit_button.config(state=NORMAL)


def get_player_entry_value():
    # read the input
    entered_value.set(player_input.get())

    # validate input and get result
    try:
        player_input_to_integer = int(player_input.get())

    except ValueError:
        game_canvas.itemconfig(response_to_player, text="You entered invalid value. \nTry again...")

    else:
        if 0 < player_input_to_integer < 101:
            result = result_from_guess(player_guess_number=player_input_to_integer)

            if result == "GUESSED":
                game_canvas.itemconfig(response_to_player,
                                       text=str("You entered " + player_input.get() + ".\n YOU WIN!!!"))

                # Player guessed the number, clear the entry and disable input
                player_input.delete(0, END)
                player_input.config(state=DISABLED)
                player_submit_button.config(state=DISABLED)

            else:
                game_canvas.itemconfig(response_to_player,
                                       text=str("You entered " + player_input.get() + ". \n" + result))
        else:
            game_canvas.itemconfig(response_to_player, text="You entered invalid value. \nTry again...")

    # clear user input for the next try
    player_input.delete(0, END)


def result_from_guess(player_guess_number):
    if player_guess_number > number_to_guess:
        return "TOO HIGH. Try again."
    elif int(player_guess_number) < number_to_guess:
        return "TOO LOW. Try again."
    else:
        return "GUESSED"


# Create Object
game_window = Tk()

# set game window title
game_window.title("Guess the number by Geri!")

# Set geometry
game_window.geometry("600x600")

# Add image file for background
bg_image = PhotoImage(file="images/background.png")

# Create Canvas
game_canvas = Canvas(game_window, width=600, height=600)
game_canvas.pack(fill="both", expand=True)

# Display image
game_canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Create the heading for the game
game_canvas.create_text(300, 30, text="GUESS THE NUMBER FROM 1 TO 100 ", font=("Times New Roman", 16), fill="black")

# Define variables:
entered_value = tk.IntVar()

# Create textbox for user input
player_input = tk.Entry(game_window, width=3, font=("Times New Roman", 50))

# Create response to the input
response_to_player = game_canvas.create_text(300, 350, width=250, text="", font=("Times New Roman", 15), fill="black")
game_window.bind('<Return>', lambda submit_pressed: get_player_entry_value())

# Create Buttons
player_submit_button = tk.Button(
    game_window,
    font=("Times New Roman", 15),
    text="GUESS",
    foreground="#20500D",
    background="#DBF7D0",
    command=get_player_entry_value
)
restart_game_button = tk.Button(
    game_window,
    font=("Times New Roman", 15),
    text="RESTART",
    foreground="#20500D",
    command=start_new_game
)
exit_game_button = tk.Button(
    game_window,
    font=("Times New Roman", 15),
    text="EXIT",
    foreground="black",
    command=game_window.destroy
)

# Display textbox and buttons:
player_input_textbox_canvas = game_canvas.create_window(250, 150, anchor="nw", window=player_input)
player_submit_button_canvas = game_canvas.create_window(260, 250, anchor="nw", window=player_submit_button)
restart_game_button_canvas = game_canvas.create_window(200, 440, anchor="nw", window=restart_game_button)
exit_game_button_canvas = game_canvas.create_window(350, 440, anchor="nw", window=exit_game_button)

# Start the game
start_new_game()

# Execute Tkinter
game_window.mainloop()
