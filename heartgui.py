
import turtle

def draw_heart():
    t = turtle.Turtle()
    t.fillcolor("red")
    t.begin_fill()
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()
    turtle.done()

if __name__ == "__main__":
    draw_heart()
