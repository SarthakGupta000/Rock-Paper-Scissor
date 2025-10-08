# Scoring system is not working properly yet since variables are not updating correctly.
# Quit button does not end game properly, just displays final score.
import tkinter as tk
from random import choice as rc
from time import sleep as ts
import sys

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x400")

label = tk.Label(window, text="")
label.pack(pady=20)
p_score = 0
a_score = 0

done = []
buttons = ["Rock", "Paper", "Scissors"]

def end_game():
    print("Exiting in 3 seconds...")
    ts(3)
    window.destroy()
    sys.exit()

quit_btn = tk.Button(window, text="Quit", command=end_game)
quit_btn.pack(pady=20)

def add_func(name):
    done.append(name)
    curr_btn = done[-1]
    ai_btn = rc(buttons)
    label.config(text=f"AI choses {ai_btn}\nYou chose {curr_btn}")
    if curr_btn == ai_btn:
        label.config(text=f"AI choses {ai_btn}\nYou chose {curr_btn}\nIt's a tie!")
    elif (curr_btn == "Rock" and ai_btn == "Scissors") or (curr_btn == "Paper" and ai_btn == "Rock") or (curr_btn == "Scissors" and ai_btn == "Paper"):
        label.config(text=f"AI choses {ai_btn}\nYou chose {curr_btn}\nYou win!")
    else:
        label.config(text=f"AI choses {ai_btn}\nYou chose {curr_btn}\nYou lose!")

for btn in buttons:
    button = tk.Button(window, text=btn, command=lambda b=btn: add_func(b))
    button.pack(pady=10)


print(done)

window.mainloop()