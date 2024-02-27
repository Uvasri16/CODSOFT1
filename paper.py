
import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose {computer_choice}. {result}")

def on_rock():
    play_game('rock')

def on_paper():
    play_game('paper')

def on_scissors():
    play_game('scissors')

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(bg='lightblue')  # Set background color for the window

# Create widgets
rock_button = tk.Button(root, text="Rock", command=on_rock, bg='lightgreen')  # Set background color for the button
paper_button = tk.Button(root, text="Paper", command=on_paper, bg='lightcoral')  # Set background color for the button
scissors_button = tk.Button(root, text="Scissors", command=on_scissors, bg='lightyellow')  # Set background color for the button
result_label = tk.Label(root, text="Choose your move!", bg='lightblue')  # Set background color for the label

# Pack widgets
rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissors_button.pack(pady=5)
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()