import tkinter as tk

class MessiAnimation:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()
        self.messi_image = tk.PhotoImage(file="Lionel-Messi-Argentina-2022-FIFA-World-Cup_(cropped).jpg")
        self.messi = self.canvas.create_image(200, 200, image=self.messi_image)
        self.dx = 1  # Initial speed in x direction
        self.dy = 1  # Initial speed in y direction
        self.move_messi()

    def move_messi(self):
        self.canvas.move(self.messi, self.dx, self.dy)
        pos = self.canvas.coords(self.messi)
        if pos[0] <= 0 or pos[2] >= 400:  # If Messi hits left or right edge
            self.dx *= -1  # Reverse x direction
        if pos[1] <= 0 or pos[3] >= 400:  # If Messi hits top or bottom edge
            self.dy *= -1  # Reverse y direction
        self.master.after(10, self.move_messi)  # Move Messi every 10 milliseconds

def main():
    root = tk.Tk()
    root.title("Lionel-Messi-Argentina-2022-FIFA-World-Cup_(cropped).jpg")
    animation = MessiAnimation(root)
    root.mainloop()

if __name__ == "__main__":
    main()
