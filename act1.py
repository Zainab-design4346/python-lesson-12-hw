import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(600, 600)
poly=turtle.Turtle()
side= 6
len= 100
a= 360.0/side
for i in range(side):
    poly.forward(len)
    poly.right(a)

turtle.done()
