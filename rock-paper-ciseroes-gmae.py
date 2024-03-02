import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock, Paper, Scissors Game")
        self.master.geometry("400x250")

        self.player_score = 0
        self.computer_score = 0

        self.player_choice = tk.StringVar()
        self.computer_choice = tk.StringVar()

        tk.Label(master, text="Player Score:").grid(row=0, column=0)
        tk.Label(master, text=f"{self.player_score}").grid(row=0, column=1)

        tk.Label(master, text="Computer Score:").grid(row=1, column=0)
        tk.Label(master, text=f"{self.computer_score}").grid(row=1, column=1)

        tk.Label(master, text="Choose your weapon:").grid(row=2, column=0)

        rock_button = tk.Radiobutton(master, text="Rock", variable=self.player_choice, value="rock")
        rock_button.grid(row=3, column=0)

        paper_button = tk.Radiobutton(master, text="Paper", variable=self.player_choice, value="paper")
        paper_button.grid(row=3, column=1)

        scissors_button = tk.Radiobutton(master, text="Scissors", variable=self.player_choice, value="scissors")
        scissors_button.grid(row=3, column=2)

        tk.Button(master, text="Play", command=self.play).grid(row=4, column=1)

    def play(self):
        self.computer_choice.set(random.choice(["rock", "paper", "scissors"]))

        if self.player_choice.get() == self.computer_choice.get():
            tk.Label(self.master, text="It's a tie!").grid(row=5, column=1)
        elif (self.player_choice.get() == "rock" and self.computer_choice.get() == "scissors") or \
             (self.player_choice.get() == "paper" and self.computer_choice.get() == "rock") or \
             (self.player_choice.get() == "scissors" and self.computer_choice.get() == "paper"):
            self.player_score += 1
            tk.Label(self.master, text=f"You win! {self.player_score} to {self.computer_score}").grid(row=5, column=1)
        else:
            self.computer_score += 1
            tk.Label(self.master, text=f"Computer wins! {self.computer_score} to {self.player_score}").grid(row=5, column=1)

root = tk.Tk()
game = RockPaperScissorsGame(root)
root.mainloop()