import random
import tkinter as tk
from tkinter import messagebox

def User(choice):
    return choice

def Computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def winner(user, Computers_Choice):
    if user == Computers_Choice:
        return 'Tie'
    elif (user == 'rock' and Computers_Choice == 'scissors') or \
         (user == 'paper' and Computers_Choice == 'rock') or \
         (user == 'scissors' and Computers_Choice == 'paper'):
        return 'user'
    else:
        return 'Computer'

def display_winners(user, Computers_Choice, Winner):
    result = f'You Chose: {user}\n'
    result += f'Computer Chose: {Computers_Choice}\n'
    if Winner == 'Tie':
        result += 'It is a tie.'
    elif Winner == 'user':
        result += 'You are the Winner.'
    else:
        result += 'Computer is the Winner.'
    return result

def play(choice):
    global user_score, computer_score
    user = User(choice)
    Computers_Choice = Computer_choice()
    Winner = winner(user, Computers_Choice)

    if Winner == 'user':
        user_score += 1
    elif Winner == 'Computer':
        computer_score += 1

    result = display_winners(user, Computers_Choice, Winner)
    result += f'\n\nScore: You {user_score} - Computer {computer_score}'
    messagebox.showinfo("Result", result)

def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    messagebox.showinfo("Reset", "Scores have been reset.")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Initialize scores
user_score = 0
computer_score = 0

# Create and place widgets
tk.Label(root, text="Choose one:").pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

rock_button = tk.Button(buttons_frame, text="Rock", command=lambda: play('rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(buttons_frame, text="Paper", command=lambda: play('paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(buttons_frame, text="Scissors", command=lambda: play('scissors'))
scissors_button.grid(row=0, column=2, padx=10)

reset_button = tk.Button(root, text="Reset Scores", command=reset_scores)
reset_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
