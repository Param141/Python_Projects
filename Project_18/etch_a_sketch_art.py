# we would like to draw a simple art piece using the turtle module in Python.
# This code will create a simple etch-a-sketch style drawing.

from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10 # Turn left by 10 degrees
    tim.setheading(new_heading)       # or simply tim.left(10) we uses left function 

def turn_right():
    new_heading = tim.heading() - 10 # Turn left by 10 degrees
    tim.setheading(new_heading)  

def clear_screen():
    tim.clear() # Clear the drawing
    tim.penup() # Lift the pen to not draw while moving
    tim.home() # Return to the starting position
    tim.pendown() # Put the pen down to draw again 

screen.listen()
screen.onkey(move_forward, "w") # Move forward with 'w'
screen.onkey(move_backward, "s") # Move backward with 's'
screen.onkey(turn_left, "a") # Turn left with 'a' 
screen.onkey(turn_right, "d") # Turn right with 'd'
screen.onkey(clear_screen, "c") # Clear the screen with 'c' .take the turtle to the home position
screen.exitonclick() # Exit on click
