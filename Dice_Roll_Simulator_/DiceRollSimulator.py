import tkinter as tk
import random

def roll_dice():
    # Define colors for each number on the dice
    colors = {
        1: "red",
        2: "blue",
        3: "green",
        4: "orange",
        5: "purple",
        6: "brown"
    }

    # Get a random number between 1 and 6
    dice_number = random.randint(1, 6)

    # Update the label text and color based on the rolled number
    lbl_dice.config(text=str(dice_number), fg=colors[dice_number])

root = tk.Tk()
root.title("Dice Roll Simulator")

lbl_title = tk.Label(root, text="Dice Roll Simulator", font=("Helvetica", 18))
lbl_title.pack(pady=20)

lbl_dice = tk.Label(root, text="", font=("Helvetica", 100), padx=50, pady=20)
lbl_dice.pack()

btn_roll = tk.Button(root, text="Roll Dice", command=roll_dice)
btn_roll.pack(pady=20)

root.mainloop()

