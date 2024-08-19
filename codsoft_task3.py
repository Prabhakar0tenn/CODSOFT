import tkinter as tk
import random

def decide_winner(player_choice, ai_choice):
    if player_choice == ai_choice:
        return "It's a draw!", 0, 0
    elif (player_choice == 'Rock' and ai_choice == 'Scissors') or \
         (player_choice == 'Scissors' and ai_choice == 'Paper') or \
         (player_choice == 'Paper' and ai_choice == 'Rock'):
        return "You won!", 1, 0
    else:
        return "AI wins!", 0, 1

def start_game(player_choice):
    global player_score, ai_score
    ai_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    outcome, player_pts, ai_pts = decide_winner(player_choice, ai_choice)
    player_score += player_pts
    ai_score += ai_pts
    outcome_label.config(text=f"AI selected: {ai_choice}\n{outcome}")
    scoreboard_label.config(text=f"Score - Player: {player_score}  AI: {ai_score}")

def handle_choice(player_choice):
    start_game(player_choice)
    replay_button.pack(pady=15)

def restart_game():
    global player_score, ai_score
    player_score = 0
    ai_score = 0
    outcome_label.config(text="")
    scoreboard_label.config(text=f"Score - Player: {player_score}  AI: {ai_score}")
    replay_button.pack_forget()

player_score = 0
ai_score = 0

app = tk.Tk()
app.title("Rock vs Paper vs Scissors")
app.configure(background='#4CAF50')  # Dark green background

prompt_label = tk.Label(app, text="Choose Rock, Paper, or Scissors:", font=('Courier', 18, 'bold'), bg='#4CAF50', fg='white')
prompt_label.pack(pady=20)

rock_btn = tk.Button(app, text="Rock", width=12, command=lambda: handle_choice('Rock'), bg='#FF5733', fg='black')  # Coral button with black text
rock_btn.pack(pady=8)

paper_btn = tk.Button(app, text="Paper", width=12, command=lambda: handle_choice('Paper'), bg='#FF5733', fg='black')
paper_btn.pack(pady=8)

scissors_btn = tk.Button(app, text="Scissors", width=12, command=lambda: handle_choice('Scissors'), bg='#FF5733', fg='black')
scissors_btn.pack(pady=8)

outcome_label = tk.Label(app, text="", font=('Courier', 16), bg='#4CAF50', fg='white')  # White text on dark green background
outcome_label.pack(pady=25)

scoreboard_label = tk.Label(app, text=f"Score - Player: {player_score}  AI: {ai_score}", font=('Courier', 16), bg='#4CAF50', fg='white')
scoreboard_label.pack(pady=15)

replay_button = tk.Button(app, text="Play Again", width=12, command=restart_game, bg='#FF5733', fg='black')

app.mainloop()
