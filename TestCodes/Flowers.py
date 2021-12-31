#-------------- Libs Import---------------
import turtle

#------------------- Function Definition----------
tur = turtle.Turtle()
scr = turtle.Screen()

scr.bgcolor('black') #screenbgcolor
tur.speed(0) #still screen

col = ['yellow', 'red', 'pink', 'cyan', 'green', 'blue'] #ColorInsertion

for i in range(120):
    tur.pencolor(col[i%6])
    tur.circle(190-i/2,90)
    tur.lt(90)
    tur.circle(190 - i / 3, 90)
    tur.lt(60)

scr.exitonclick()