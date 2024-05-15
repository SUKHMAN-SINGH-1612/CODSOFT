"""
Rock-Paper-Scissors Game
User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) forthe computer.
Game Logic: Determine the winner based on the user's choice and thecomputer's choice.
Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.
Display the result, whether the user wins, loses, or it's a tie.
Score Tracking (Optional): Keep track of the user's and computer's scores formultiple rounds.
Play Again: Ask the user if they want to play another round.
User Interface: Design a user-friendly interface with clear instructions and feedback.
"""
import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.user_score = 0
        self.computer_score = 0

        self.user_choice_var = tk.StringVar()
        self.computer_choice_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.score_var = tk.StringVar()

        root.title("Rock Paper Scissors")

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.choices = ['rock', 'paper', 'scissors']
        self.colors = ['red', 'green', 'blue']
        for choice, color in zip(self.choices, self.colors):
            button = tk.Button(self.frame, 
                               text=choice.upper(), 
                               fg=color,
                               font=('Arial', 20),
                               command=lambda choice=choice: self.play_game(choice))
            button.pack(side=tk.LEFT, padx=10, pady=10)

        self.user_choice_label = tk.Label(root, textvariable=self.user_choice_var, font=('Arial', 15))
        self.user_choice_label.pack(pady=10)

        self.computer_choice_label = tk.Label(root, textvariable=self.computer_choice_var, font=('Arial', 15))
        self.computer_choice_label.pack(pady=10)

        self.result_label = tk.Label(root, textvariable=self.result_var, font=('Arial', 15))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, textvariable=self.score_var, font=('Arial', 15))
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(root, 
                                           text="PLAY AGAIN", 
                                           font=('Arial', 20),
                                           command=self.reset_game)
        self.play_again_button.pack(pady=10)

        messagebox.showinfo("Instructions", "Welcome to Rock Paper Scissors!\n\n"
                                            "Here are the rules:\n"
                                            "Rock beats Scissors\n"
                                            "Scissors beats Paper\n"
                                            "Paper beats Rock\n\n"
                                            "Choose your option and see if you can beat the computer!")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        if (user_choice == 'rock' and computer_choice == 'scissors') or \
           (user_choice == 'scissors' and computer_choice == 'paper') or \
           (user_choice == 'paper' and computer_choice == 'rock'):
            return 'user'
        else:
            return 'computer'
        
    def reset_game(self):
        self.user_choice_var.set("")
        self.computer_choice_var.set("")
        self.result_var.set("")

    def play_game(self, user_choice):
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, computer_choice)
    
        if winner == 'user':
            self.user_score += 1
        elif winner == 'computer':
            self.computer_score += 1
    
        self.user_choice_var.set(f"User chose {user_choice}")
        self.computer_choice_var.set(f"Computer chose {computer_choice}")
        self.result_var.set(f"{winner.capitalize()} wins!")
        self.score_var.set(f"Score: User - {self.user_score}, Computer - {self.computer_score}")

root = tk.Tk()
game = RockPaperScissors(root)
root.mainloop()