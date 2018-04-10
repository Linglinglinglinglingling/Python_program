import turtle
def fractals(turtle_object,order,length):
    if order==0:
        turtle_object.forward(length)
    else:
        for angle in [60,-120,60,0]:
            fractals(turtle_object,order-1,length/3)
            turtle_object.left(angle)

a=turtle.Screen()
a.bgcolor('lightgreen')
b=turtle.Turtle()
b.shape('blank')
b.color('blue')
b.speed(10)
b.pendown()
fractals(b,4,300)
a.mainloop()
