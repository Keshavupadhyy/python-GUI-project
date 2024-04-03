import tkinter as tk
from tkinter import filedialog
import pygame
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class AudioPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Player with Visualization")
        self.root.geometry("400x300")

        self.load_button = tk.Button(self.root, text="Load", command=self.load_audio)
        self.load_button.pack(pady=10)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_audio, state=tk.DISABLED)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_audio, state=tk.DISABLED)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_audio, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.audio_file = None
        self.is_playing = False

        self.fig, self.ax = plt.subplots()
        self.ax.set_axis_off()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)

    def load_audio(self):
        self.audio_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if self.audio_file:
            self.play_button.config(state=tk.NORMAL)

    def play_audio(self):
        if not self.is_playing:
            pygame.mixer.init()
            pygame.mixer.music.load(self.audio_file)
            pygame.mixer.music.play()
            self.is_playing = True
            self.play_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
            self.animate_visualization()

    def pause_audio(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            self.pause_button.config(state=tk.DISABLED)
            self.play_button.config(state=tk.NORMAL)

    def stop_audio(self):
        if self.is_playing:
            pygame.mixer.music.stop()
            self.is_playing = False
            self.pause_button.config(state=tk.DISABLED)
            self.play_button.config(state=tk.NORMAL)

    def animate_visualization(self):
        while pygame.mixer.music.get_busy():
            pygame.event.poll()
            audio_data = pygame.mixer.music.get_busy()
            self.ax.clear()
            self.ax.bar(range(len(audio_data)), audio_data, color='blue')
            self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayer(root)
    root.mainloop()
