#ex3
import turtle
bob=turtle.Turtle()
ace=turtle.Turtle()

def polygon(distance,sides):
    angle=360/sides
    
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
   

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(d,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(5):
        bob.forward(d)
        bob.right(144)
    bob.end_fill()

def explosion(d,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(8):
        bob.forward(d)
        bob.right(135)
    bob.end_fill()

def starship():

    for times in range(100):
        c = ( times*2,0,times*2)
        
