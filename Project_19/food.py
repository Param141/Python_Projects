# will create a Food class which renders the food on the screen and  each time the snake touches the food it gets generated to a random new location on screen

from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__() # inherited Turtle inside the food class on which we are working (now can use all the methods and attributes of turtle class in here)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) # this allow us to strech the turtle along its height and width
        # turtle is of 20*20 size streched it to half length so now of 10*10 size 
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
            # method to make food go to random location 
           random_x=random.randint(-280,280) #screen is 600*600 so -300 to 300 in x and y we don't want food just near the wall so generating random postion little ahead
           random_y=random.randint(-280,280)
           self.goto(random_x,random_y)

    
       