import turtle
turtle.setup(900,1200,200,200)
turtle.penup()
turtle.fd(-50)
turtle.pendown()
turtle.pensize(5)
turtle.pencolor("violet")
turtle.seth(360)
turtle.circle(10,360)
s=50
for i in range(8):
    s=50+i*40
    turtle.pencolor("violet")
    turtle.seth(270)
    turtle.fd(5)
    turtle.pencolor("white")
    turtle.seth(270)
    turtle.fd(35)
    turtle.pencolor("violet")
    turtle.seth(0)
    turtle.circle(s,360)
