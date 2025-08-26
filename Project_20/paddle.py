from turtle import Turtle

class Paddle(Turtle): # need to inherit from the Turtle class in order to use its property for making the paddle 
    def __init__(self,position):
        super().__init__()
        # paddle = Turtle() Paddle class is same as Turtle class so get rid of this line entirely and use self instead of paddle because we are inside paddle class so can tap into attributes and methods using self keyword
        self.shape("square") #all turtles start at 20*20 ( need to strech it along width by 5 and leave as it is along length)
        self.color("white") # to make sure the paddle is visible when we actually run the code 
        self.shapesize(stretch_wid=5,stretch_len=1) 
        self.penup() # in order to make the paddle go to the right boundary of the screen first need to penup and then use goto function 
        self.goto(position) # padale going to the position sent as argument 

    
    # defyning go_up and go_down as method inside Paddle class but method would always have first attribute as self and  also would replace paddle. with self.
    
    def go_up(self):
        
    # will gonna move the paddle to new position (by moving in y dirn only on clicking up arrow key and keeping x position constant)
        new_y=self.ycor()+20 # will gonna move 20 positions up in the y axis 
        self.goto(self.xcor(),new_y) # kept the current paddle x cordinate same but changed only the y cordinate 


    def go_down(self):
        new_y=self.ycor()-20 # going 20 positions down 
        self.goto(self.xcor(),new_y)