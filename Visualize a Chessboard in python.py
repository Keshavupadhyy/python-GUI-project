import numpy as np
import matplotlib.pyplot as plt

def draw_chessboard():
    # Create an 8x8 array filled with zeros (representing empty squares)
    board = np.zeros((8, 8))

    # Color the squares of the chessboard
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                board[i][j] = 1

    # Create a plot
    plt.figure(figsize=(6,6))
    plt.imshow(board, cmap='binary', origin='lower')

    # Add labels to the axes to represent the chessboard coordinates
    plt.xticks(np.arange(8), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    plt.yticks(np.arange(8), range(1, 9))

    plt.show()

# Call the function to draw the chessboard
draw_chessboard()
