#exploring r,g b
from ex3 import*
turtle.colormode(255)
bob.speed(0)

for times in range(255):
    bob.color(255-times,255-times,255-times)
    bob.circle(255-times)
    bob.right(20)
            
