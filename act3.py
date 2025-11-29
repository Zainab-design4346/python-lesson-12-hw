import turtle
window= turtle.Screen()
window.bgcolor("pink")
window.title("Turtle")
p=turtle.Turtle()
s=0

while True:
    for i in range(15):
        p.forward(s+1)
        p.left(24)
        s=s-5
    s=s+1
