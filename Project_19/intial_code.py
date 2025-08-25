from turtle import Turtle, Screen
import time 

screen = Screen()
screen.title("Snake Game") # Set the title of the game window
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)  # Turn off the screen updates for smoother animation 


# create the snake body using 3 turtles in the shape of a square lined up next to each other

# segment_1= Turtle("square")
# segment_1.color("white")  # in order to see the snake on the black background

# segment_2= Turtle("square")
# segment_2.color("white") 
# segment_2.goto(-20, 0)  # Position the second segment next to the first ( moving left by 20 units in order to line them up and not overlap)

# segment_3= Turtle("square")
# segment_3.color("white") 
# segment_3.goto(-40, 0)  # Position the third segment next to the second (moving left by another 20 units)

# or a more easier way is to create a tuple for the positons and then use a for loop to create the segments

positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []  # List to hold the segments of the snake
# Create the segments using a for loop
for i in positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()  # Prevent the turtle from drawing lines when moving (call before the goto line to prevent from even the starting line to appear )
    segment.goto(i)  # Set the position of each segment
    
    segment.speed("fastest")  # Set the speed to the fastest to avoid flickering
    segments.append(segment)  # Add the segment to the list

# screen.update()  # Update the screen to show the initial state of the snake


# Now would move the snake segments in a loop 
game_is_on = True  # Variable to control the game loop
while game_is_on:
    screen.update()  # Update the screen to reflect changes
    time.sleep(0.1)  # Pause for a short duration to control the speed of the game
    # Here you can add logic to control the snake's movement, such as responding to key presses or moving automatically.
    
    for seg_num in range(len(segments)-1,0,-1): # basically is start,stop,step inside the range fucntion we can't mention  it because range doesn' take any parameter 
        # moving from last segment to first one 
        new_x=segments[seg_num-1].xcor() # get hold of second to last segment 
        new_y=segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y) # telling the last segment to go to the positon of second to last segment 
    segments[0].forward(20) # moving the first segment by 20 units outside the loop and other segments will follow it because of the above written code

        
 



screen.exitonclick()  # Wait for a click to close the window 