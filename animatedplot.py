import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to update the plot in each animation frame
def update(frame):
    # Clear the previous plot
    plt.clf()

    # Generate data for the new frame
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x + frame * 0.1)

    # Plot the updated data
    plt.plot(x, y, label='Sin(x + t)')
    plt.title('Animated Sinusoidal Function')
    plt.xlabel('x')
    plt.ylabel('sin(x + t)')
    plt.legend()

# Set up the figure and axis
fig, ax = plt.subplots()

# Create the animation with a specified interval (in milliseconds)
animation = FuncAnimation(fig, update, frames=range(100), interval=100)

# Display the animated plot
plt.show()
