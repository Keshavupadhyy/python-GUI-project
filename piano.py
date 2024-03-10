import tkinter as tk
from pygame import mixer

def play_sound(note):
    sound_file = f"sounds/{note}.wav"
    mixer.Sound(sound_file).play()

def create_piano():
    root = tk.Tk()
    root.title("Piano")

    # Function to bind key press events
    def key_pressed(event):
        note = event.char.upper()
        play_sound(note)

    # Create piano keys
    keys = "CDEFGAB"
    for key in keys:
        tk.Button(root, text=key, width=5, height=10, command=lambda k=key: play_sound(k)).pack(side=tk.LEFT)
        root.bind(key, key_pressed)

    # Create a Quit button
    tk.Button(root, text="Quit", command=root.destroy).pack()

    # Initialize mixer for sound
    mixer.init()

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    create_piano()
