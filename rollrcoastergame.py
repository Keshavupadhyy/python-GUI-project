import tkinter as tk
import random

class RollerCoasterGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Roller Coaster Game")

        self.canvas = tk.Canvas(master, width=600, height=400, bg="skyblue")
        self.canvas.pack()

        self.roller_coaster = self.canvas.create_line(50, 300, 550, 300, width=5, fill="black")

        self.cart = self.canvas.create_rectangle(50, 250, 100, 300, fill="red")

        self.obstacle_width = 50
        self.obstacle_speed = 5
        self.obstacle_interval = 150
        self.obstacles = []

        self.score = 0
        self.score_label = tk.Label(master, text="Score: 0", font=("Helvetica", 14))
        self.score_label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_ride)
        self.start_button.pack()

        self.game_over = False

    def start_ride(self):
        self.game_over = False
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.obstacles = []
        self.animate_cart()

    def animate_cart(self):
        if not self.game_over:
            x1, y1, x2, y2 = self.canvas.coords(self.cart)
            if x2 < 550:
                self.canvas.move(self.cart, 5, 0)
                self.master.update()
                self.master.after(50)
                self.check_collision()
                self.create_obstacle()
                self.move_obstacles()
                self.update_score()
                self.animate_cart()
            else:
                self.game_over = True
                self.display_game_over()

    def create_obstacle(self):
        if random.randint(1, 10) == 1:
            obstacle = self.canvas.create_rectangle(600, 250, 600 + self.obstacle_width, 300, fill="green")
            self.obstacles.append(obstacle)

    def move_obstacles(self):
        for obstacle in self.obstacles:
            self.canvas.move(obstacle, -self.obstacle_speed, 0)
            if self.canvas.coords(obstacle)[2] < 0:
                self.canvas.delete(obstacle)
                self.obstacles.remove(obstacle)

    def check_collision(self):
        for obstacle in self.obstacles:
            if self.canvas.bbox(obstacle, overlapping=self.cart):
                self.game_over = True
                self.display_game_over()

    def update_score(self):
        self.score += 1
        self.score_label.config(text="Score: {}".format(self.score))

    def display_game_over(self):
        game_over_label = tk.Label(self.master, text="Game Over!", font=("Helvetica", 20, "bold"), fg="red")
        game_over_label.pack()
        restart_button = tk.Button(self.master, text="Restart", command=self.start_ride)
        restart_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    game = RollerCoasterGame(root)
    root.mainloop()
