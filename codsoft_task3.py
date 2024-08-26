import tkinter as tk
import random

def decide_winner(p_choice, a_choice):
    if p_choice == a_choice:
        return "Draw!", 0, 0
    if (p_choice == 'Rock' and a_choice == 'Scissors') or \
       (p_choice == 'Scissors' and a_choice == 'Paper') or \
       (p_choice == 'Paper' and a_choice == 'Rock'):
        return "You win!", 1, 0
    return "AI wins!", 0, 1

def play_game(p_choice):
    global p_score, a_score
    a_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    result, p_pts, a_pts = decide_winner(p_choice, a_choice)
    p_score += p_pts
    a_score += a_pts
    lbl_result.config(text=f"AI chose: {a_choice}\n{result}")
    lbl_score.config(text=f"Score - Player: {p_score}  AI: {a_score}")

def make_choice(choice):
    play_game(choice)
    btn_replay.pack(pady=15)

def reset_game():
    global p_score, a_score
    p_score = 0
    a_score = 0
    lbl_result.config(text="")
    lbl_score.config(text=f"Score - Player: {p_score}  AI: {a_score}")
    btn_replay.pack_forget()

p_score = 0
a_score = 0

app = tk.Tk()
app.title("Rock Paper Scissors")
app.configure(bg='#4CAF50')

lbl_prompt = tk.Label(app, text="Choose Rock, Paper, or Scissors:", font=('Arial', 16), bg='#4CAF50', fg='white')
lbl_prompt.pack(pady=20)

btn_rock = tk.Button(app, text="Rock", width=12, command=lambda: make_choice('Rock'), bg='#FF5733', fg='black')
btn_rock.pack(pady=5)

btn_paper = tk.Button(app, text="Paper", width=12, command=lambda: make_choice('Paper'), bg='#FF5733', fg='black')
btn_paper.pack(pady=5)

btn_scissors = tk.Button(app, text="Scissors", width=12, command=lambda: make_choice('Scissors'), bg='#FF5733', fg='black')
btn_scissors.pack(pady=5)

lbl_result = tk.Label(app, text="", font=('Arial', 14), bg='#4CAF50', fg='white')
lbl_result.pack(pady=20)

lbl_score = tk.Label(app, text=f"Score - Player: {p_score}  AI: {a_score}", font=('Arial', 14), bg='#4CAF50', fg='white')
lbl_score.pack(pady=10)

btn_replay = tk.Button(app, text="Play Again", width=12, command=reset_game, bg='#FF5733', fg='black')

app.mainloop()

