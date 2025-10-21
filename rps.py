# Hi, please check the markdown file for this code for more information.
# Later, I plan to add tkinter graphical support for better play
from sklearn.ensemble import RandomForestClassifier
import random

# rock - 0, paper - 1, scissor - 2
X = []
y = []
rounds = 0
usr = 0
ai = 0

model = RandomForestClassifier()

def play(player_pred):
    user_play = int(input("(0 - rock, 1 - paper, 2 - scissor)\n> "))
    ai_play = (player_pred + 1) % 3
    print(f"\nAI plays: {['rock','paper','scissor'][ai_play]}")

    if user_play == ai_play:
        print("It's a tie!")
        winner = None
    elif (user_play == 0 and ai_play == 2) or (user_play == 1 and ai_play == 0) or (user_play == 2 and ai_play == 1):
        print("You win!")
        winner = True
    else:
        print("AI wins!")
        winner = False
    return winner, user_play

def main():
    global rounds, usr, ai
    n = 10
    prev_user_play = random.randint(0, 2)  # dummy start

    while rounds < n:
        # Train only if we have data
        if len(X) > 3:
            model.fit(X, y)
            player_pred = model.predict([[prev_user_play]])[0]
        else:
            player_pred = random.randint(0, 2)
        
        win, user_play = play(player_pred)
        if win == True: usr += 1
        elif win == False: ai += 1
        else: pass

        # Store data: input = previous user move, output = current move
        X.append([prev_user_play])
        y.append(user_play)

        # Update for next round
        prev_user_play = user_play

        rounds += 1

    print(f"\nGame over! You: {usr}, AI: {ai}")

if __name__ == "__main__":
    main()