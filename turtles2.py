from turtle import Turtle, Screen
from random import randint, choice  as rand_choice
colors =["blue","green","red","orange"]
class MyTurtle(Turtle):
    def random_shape(self, Turtle1, Turtle2):
         self.color(rand_choice(colors))

         self.penup()
         self.setposition( randint (-200, 200), randint(-200, 200))
         self.pendown()
         self.circle(50, steps=randint(4, 12))
   
    def __init__(self):
        super().__init__()
        self.random_shape(0, 0)
        self.onclick(self.random_shape)


Turtle1 = MyTurtle()
Turtle2 = MyTurtle()



screen = Screen()

screen.mainloop()

