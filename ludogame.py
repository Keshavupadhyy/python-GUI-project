import tkinter as tk
import random

class LudoGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Ludo Game")

        self.canvas = tk.Canvas(master, width=400, height=400, bg="white")
        self.canvas.pack()

        self.create_board()
        self.create_players()
        self.current_player = 0

        self.roll_button = tk.Button(master, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()

    def create_board(self):
        # Draw the Ludo board
        self.canvas.create_rectangle(50, 50, 350, 350, outline="black", width=2)

        # Draw the cross lines
        self.canvas.create_line(200, 50, 200, 350, fill="black", width=2)
        self.canvas.create_line(50, 200, 350, 200, fill="black", width=2)

    def create_players(self):
        # Player positions
        self.player_positions = [0, 0, 0, 0]

        # Draw players on the board
        for i in range(4):
            self.draw_player(i, self.player_positions[i])

    def draw_player(self, player_id, position):
        colors = ["red", "green", "blue", "yellow"]
        x, y = self.get_player_coordinates(player_id, position)
        player_size = 20

        self.canvas.create_oval(x - player_size, y - player_size, x + player_size, y + player_size, fill=colors[player_id])

    def get_player_coordinates(self, player_id, position):
        row, col = divmod(position, 5)
        x = 50 + col * 70
        y = 50 + row * 70

        if player_id == 1:
            x += 35
        elif player_id == 2:
            y += 35
        elif player_id == 3:
            x += 35
            y += 35

        return x, y

    def roll_dice(self):
        dice_value = random.randint(1, 6)
        print(f"Player {self.current_player + 1} rolled a {dice_value}")

        # Move the player piece
        self.move_player(self.current_player, dice_value)

        # Redraw the players
        self.canvas.delete("all")
        self.create_board()
        self.create_players()

        # Check for a winner
        if max(self.player_positions) >= 25:
            print(f"Player {self.player_positions.index(max(self.player_positions)) + 1} wins!")

        # Switch to the next player
        self.current_player = (self.current_player + 1) % 4

    def move_player(self, player_id, steps):
        # Check if the move is valid
        if self.player_positions[player_id] + steps <= 25:
            self.player_positions[player_id] += steps
        else:
            print("Invalid move. Try again.")

root = tk.Tk()
ludo_game = LudoGame(root)
root.mainloop()
