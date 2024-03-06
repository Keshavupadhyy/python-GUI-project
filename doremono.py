import turtle

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(color, width, height, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x - width / 2, y - height / 2)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

def draw_doraemon():
    turtle.speed(2)
    turtle.bgcolor("#7EC8E3")  # Doraemon's color

    # Draw Doraemon's face
    draw_circle("white", 100, 0, -100)

    # Draw Doraemon's eyes
    draw_circle("blue", 15, -35, 25)
    draw_circle("blue", 15, 35, 25)

    # Draw Doraemon's pupils
    draw_circle("black", 7, -35, 25)
    draw_circle("black", 7, 35, 25)

    # Draw Doraemon's nose
    draw_circle("red", 5, 0, 0)

    # Draw Doraemon's mouth
    turtle.penup()
    turtle.goto(-30, -30)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(30, 180)

    # Draw Doraemon's whiskers
    for angle in [60, 45, 30, 0, -30, -45, -60]:
        turtle.penup()
        turtle.goto(0, 10)
        turtle.pendown()
        turtle.right(angle)
        turtle.forward(40)

    # Draw Doraemon's body
    draw_rectangle("#1294D8", 180, 120, 0, -200)

    turtle.hideturtle()
    turtle.done()

# Draw Doraemon using the Turtle module
draw_doraemon()


