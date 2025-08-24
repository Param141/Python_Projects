from turtle import Turtle, Screen
import random

is_race_on = False # variable to check if 

screen = Screen()

screen.setup(width=500, height=400) # setup method allows you to set the size of the screen . use the keyword arguments width and height to set the size of the screen.

user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ") 
# textinput method allows you to create a pop-up window that prompts the user for input. it takes two arguments: title and prompt. The title is the title of the pop-up window, and the prompt is the message that will be displayed in the window.
# it returns the input from the user as a string.
#print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"] # list of colors for the turtles
all_turtles = [] # empty list to store the turtles


for turtle_index in range(0, 6): # for loop to create 6 turtles
    new_turtle = Turtle(shape="turtle") # create a new turtle with the shape of a turtle
    new_turtle.color(colors[turtle_index]) # set the color of the turtle using the color method which takes one argument: the color of the turtle.
    new_turtle.penup() # lift the pen so that it does not draw a line when the turtle moves.
    new_turtle.goto(x=-230, y=-100 + (turtle_index * 30)) # move the turtle to the starting position using the goto method which takes two arguments: x and y coordinates.
    all_turtles.append(new_turtle) # add the new turtle to the list all_turtles

# x postion is -230 (same for all) and y position is -100 + (turtle_index * 30) to create a vertical line of turtles with a gap of 30 pixels between 
# or can declare y_positon = [-70,-40,-10,20,50,80] and then use y_position[turtle_index] to get the y position of the turtle.

# to move all the turtles forward in an random gap we would create a random number between 0 and 10 using the random module and then use the forward method to move the turtle forward by that amount.

# if user_bet: # check if the user has made a bet if yes then set is_race_on to True
if user_bet:
    is_race_on = True # set

while is_race_on: # now can start the race once the user has made a bet on any turtle
    for turtle in all_turtles: # loop through all the turtles
        random_distance = random.randint(0, 10) # generate a random distance between 0 and 10
        turtle.forward(random_distance) # move the turtle forward by the random distance

        if turtle.xcor() > 230: # check if the turtle has crossed the finish line (x coordinate > 230) as the turtle object is 40 pixels wide and the finish line is at x=230 not x=250 i.e 250 - (40/2)
            is_race_on = False # in order to stop printing again and again the turtle has crossed the finish line 
            winning_color = turtle.pencolor() # get the color of the turtle that has crossed the finish
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:  
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break # exit the for loop since the race is over


    
    random_distance = random.randint(0, 10) # generate a random distance between 0 and 10
    for turtle in all_turtles: # loop through all the turtles
        turtle.forward(random_distance) # move the turtle forward by the random distance
        
            
    


# tim= Turtle() # now would want to go at start of the screen using the goto method which takes two arguments x and y coordinates.
# tim.shape("turtle") # shape method allows you to set the shape of the turtle. it takes one argument: the shape of the turtle.
# tim.penup() # penup method allows you to lift the pen so that it does not draw a line when the turtle moves.
# tim.goto(x=-230, y=-100) # goto method allows you to move the turtle



screen.exitonclick() 