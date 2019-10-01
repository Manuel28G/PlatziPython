import turtle

forward = 20
rotationLeft = 70
sumForward = 1
window = turtle.Screen()
david = turtle.Turtle()
for i in range(100):
    david.forward(forward)
    david.left(rotationLeft)
    forward += sumForward
turtle.mainloop()



