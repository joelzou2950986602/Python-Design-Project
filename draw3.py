#function
from ex3 import*
bob.speed(0)
turtle.colormode(255)
turtle.bgcolor('black')

x = 1

while x < 400:
    for c in["orchid","darkorchid","fuchsia"]:
        bob.color(c)
        bob.forward(50 + x)
        bob.right(90.911)

        x = x+1
    
    
