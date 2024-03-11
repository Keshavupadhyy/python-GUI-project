import turtle
import math
import colorsys

# Function to draw a colorful spiral
def draw_spiral(num_lines=300, line_length=1, angle=30, color_shift=10):
    for _ in range(num_lines):
        turtle.forward(line_length)
        turtle.right(angle)
        line_length += 1
        hue = (turtle.heading() / 360.0) + color_shift
        turtle.color(colorsys.hsv_to_rgb(hue, 1.0, 1.0))

# Set up the turtle screen
turtle.speed(0)  # Set the drawing speed to the maximum

# Draw a colorful spiral
draw_spiral()

# Close the turtle graphics window on click
turtle.exitonclick()
