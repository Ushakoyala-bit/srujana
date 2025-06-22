import turtle
screen=turtle.Screen()
screen.setup(500, 600,startx=0,starty=10)
squary=turtle.Turtle()
squary.speed(10)

for i in range(500):
    squary.forward(i)
    squary.left(90)


