from turtle import *
from random import randint, choice
colors =["blue","green","red","orange","white"]
speed(0)
circle(randint(10,50), steps=randint(4, 10))
for i in range(10):
   penup()
   setposition(randint(-200, 200), randint(-200,200))
   pendown()
  #color(choice(colors))
   pencolor(choice(colors))
   fillcolor(choice(colors))
   pensize(3)
   color(choice(colors))
   begin_fill()
   circle(randint(10, 50), steps=randint(4, 10))
   end_fill()
   left(randint(5, 10))
done()