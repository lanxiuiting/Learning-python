#e8.1DrawKoch.py
import turtle
def koch(size,n):
    if n==0:
       turtle.fd(size)
    else:
       for angle in [0,60,-120,60]:
           turtle.left(angle)
           koch(size/3,n-1)
def main():
    turtle.setup(800,400)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-300,-50)
    turtle.pendown()
    turtle.pensize(2)
    koch(300 ,2)
    turtle.hideturtle()
main()