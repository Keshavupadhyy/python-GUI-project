import tkinter as tk
from tkinter import messagebox
import random

class LudoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Ludo")
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()
        self.players = ['Red', 'Green', 'Blue', 'Yellow']
        self.player_positions = {player: 0 for player in self.players}
        self.colors = {'Red': 'red', 'Green': 'green', 'Blue': 'blue', 'Yellow': 'yellow'}
        self.draw_board()
        self.draw_pieces()
        self.current_player = random.choice(self.players)
        self.roll_button = tk.Button(master, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()

    def draw_board(self):
        for i in range(0, 4):
            for j in range(0, 4):
                if (i == 1 and j == 1) or (i == 1 and j == 2) or (i == 2 and j == 1) or (i == 2 and j == 2):
                    color = "white"
                else:
                    color = "lightgreen"
                self.canvas.create_rectangle(i * 100, j * 100, (i + 1) * 100, (j + 1) * 100, fill=color)

    def draw_pieces(self):
        for player, pos in self.player_positions.items():
            color = self.colors[player]
            if pos != -1:
                x, y = self.get_coordinates(pos)
                self.canvas.create_oval(x, y, x + 20, y + 20, fill=color)

    def get_coordinates(self, position):
        x = position % 4
        y = position // 4
        if y % 2 == 1:
            x = 3 - x
        return x * 100 + 40, y * 100 + 40

    def roll_dice(self):
        dice_roll = random.randint(1, 6)
        messagebox.showinfo("Dice Roll", f"{self.current_player} rolled {dice_roll}")
        self.move_piece(self.current_player, dice_roll)

    def move_piece(self, player, steps):
        current_position = self.player_positions[player]
        new_position = current_position + steps

        if new_position > 15:
            new_position = 15

        self.player_positions[player] = new_position
        self.canvas.delete(player)
        x, y = self.get_coordinates(new_position)
        self.canvas.create_oval(x, y, x + 20, y + 20, fill=self.colors[player], tags=player)

        if new_position == 15:
            messagebox.showinfo("Winner", f"{player} wins!")
            self.roll_button.config(state="disabled")
        else:
            self.current_player = self.get_next_player(player)

    def get_next_player(self, current_player):
        index = self.players.index(current_player)
        return self.players[(index + 1) % len(self.players)]

def main():
    root = tk.Tk()
    ludo_gui = LudoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
