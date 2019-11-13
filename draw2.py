#function file
from ex3 import*
turtle.colormode(255)
turtle.bgcolor('black')
bob.speed(0)


for times in range(120):
    bob.color(times,0,255-times)
    bob.circle(times+1)
    bob.right(60)



