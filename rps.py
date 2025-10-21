import tkinter as tk
from sklearn.ensemble import RandomForestClassifier
import random

X = []
y = []
rounds = 0
usr = 0
ai = 0
n = 10
prev_user_play = random.randint(0, 2)
model = RandomForestClassifier()

window = tk.Tk()
window.title("Rock Paper Scissors - AI Trainer")
window.geometry("400x400")
window.resizable(False, False)

head = tk.Label(window, text="Rock-Paper-Scissors", bg="blue", fg="white", font=("Arial", 16), pady=10)
head.pack(fill="x")

info_label = tk.Label(window, text="Choose your move:", font=("Arial", 12))
info_label.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(window, text="You: 0 | AI: 0", font=("Arial", 12, "bold"))
score_label.pack(pady=10)

def quitting():
    global window
    window.destroy()

quit = tk.Button(text = "QUIT", command = quitting)
quit.pack(pady=10)

def get_ai_play(prev_user_play):
    if len(X) > 3:
        model.fit(X, y)
        player_pred = model.predict([[prev_user_play]])[0]
    else:
        player_pred = random.randint(0, 2)
    ai_play = (player_pred + 1) % 3
    return ai_play

def play(user_play):
    global rounds, usr, ai, prev_user_play, n

    if rounds >= n:
        result_label.config(text=f"Game over! Final score - You: {usr}, AI: {ai}")
        return

    ai_play = get_ai_play(prev_user_play)

    moves = ["Rock", "Paper", "Scissors"]
    result_text = f"You chose {moves[user_play]}, AI chose {moves[ai_play]}.\n"

    if user_play == ai_play:
        result_text += "It's a tie!"
    elif (user_play == 0 and ai_play == 2) or (user_play == 1 and ai_play == 0) or (user_play == 2 and ai_play == 1):
        usr += 1
        result_text += "You win!"
    else:
        ai += 1
        result_text += "AI wins!"

    X.append([prev_user_play])
    y.append(user_play)
    prev_user_play = user_play
    rounds += 1

    result_label.config(text=result_text)
    score_label.config(text=f"You: {usr} | AI: {ai}")

    if rounds >= n:
        result_label.config(text=f"Game over! Final score - You: {usr}, AI: {ai}")
        return

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play(0))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play(1))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play(2))
scissors_btn.grid(row=0, column=2, padx=5)

window.mainloop()
