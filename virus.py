from turtle import *

speed(0)
color('cyan')
bgcolor('black')

b=200

penup()
goto(300,80)
pendown()

while b > 0:
    left(b)
    forward(b * 3)
    b=b-1

exitonclick()