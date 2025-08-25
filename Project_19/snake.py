from turtle import Turtle 
POSITIONS = [(0, 0), (-20, 0), (-40, 0)] # making the starting positions as constant that's why written in capital 
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

# create a new snake object using the starting positionos declared above 
class Snake:
    def __init__(self):
        # will determine what should happen when we intialize new snake object
        self.segments = [] # attribute associated with the snake class 
        self.create_snake() # creating a method 

    def create_snake(self):
        for i in POSITIONS: 
         self.add_segment(i) # add new segment everytime 
    
    def add_segment(self,positon):
         segment = Turtle("square")
         segment.color("white")
         segment.penup()  # Prevent the turtle from drawing lines when moving (call before the goto line to prevent from even the starting line to appear )
         segment.goto(positon)  # Set the position of each segment
        
         segment.speed("fastest")  # Set the speed to the fastest to avoid flickering
         self.segments.append(segment)  # Add the segment to the list
       
    


    def extend(self):
       # creating a method to add a new segment everytime snake eats the food or better say collide with the food turtle 
       self.add_segment(self.segments[-1].position()) # getting hold of the last segment in the snake body and adding a new segment in its positionn

    def move(self):
        
     for seg_num in range(len(self.segments)-1,0,-1): # basically is start,stop,step inside the range fucntion we can't mention  it because range doesn' take any parameter 
        # moving from last segment to first one 
        new_x=self.segments[seg_num-1].xcor() # get hold of second to last segment 
        new_y=self.segments[seg_num-1].ycor()
        self.segments[seg_num].goto(new_x,new_y) # telling the last segment to go to the positon of second to last segment 
     self.segments[0].forward(MOVE_DISTANCE) # moving the first segment by 20 units outside the loop and other segments will follow it because of the above written code
       
    def up(self): 
       # the head can't change it directions in between the game ie it is not allowed to move to tail from front so need to make a condition for that 
       if self.segments[0].heading()!=DOWN: # when the head is not facing down  then only can move it up ( if the current heading is pointed down then it can't move up but for all other directions moving up is possibel )
           self.segments[0].setheading(UP) # take the head of the snake and set its heading to the north by turning 90 degree

    def down(self):
       if self.segments[0].heading()!=UP: # when the head is not facing down  then only can move it up ( if the current heading is pointed down then it can't move up but for all other directions moving up is possibel )
           
           self.segments[0].setheading(DOWN)
    
    def left(self):
       if self.segments[0].heading()!=RIGHT:
           self.segments[0].setheading(LEFT)
    
    def right(self):
       if self.segments[0].heading()!=LEFT: 
           
           self.segments[0].setheading(RIGHT) # usisng the anticlockwise direction 