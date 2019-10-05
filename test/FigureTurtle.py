# --*-- encoding:utf-8 --*--
import turtle

global sumForward

def main():
    sizeRectangle = int(raw_input('De que tamaño será el cuadrado?'))
    global sumForward
    sumForward = 0
    turtle.Screen()
    dave = turtle.Turtle()
    make_rectangle(dave,sizeRectangle,90)

def make_rectangle(dave,forward,rotationLeft):
    for i in range(4):
        dave.forward(forward)
        dave.left(rotationLeft)
        forward += sumForward
    turtle.mainloop()

if __name__ == '__main__':
    main()



