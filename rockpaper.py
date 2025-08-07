import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    comp_choice = random.choice(choices)

    user_label.config(text=f"You chose: {user_choice}")
    comp_label.config(text=f"Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    user_label.config(text="You chose: ")
    comp_label.config(text="Computer chose: ")
    result_label.config(text="Result:")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14)).pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Rock", width=12, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=12, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=12, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

user_label = tk.Label(root, text="You chose: ", font=("Arial", 12))
user_label.pack(pady=5)

comp_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
comp_label.pack(pady=5)

result_label = tk.Label(root, text="Result:", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)

tk.Button(root, text="Play Again", command=reset_game).pack(pady=10)

root.mainloop()
