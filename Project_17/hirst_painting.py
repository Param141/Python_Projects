# import colorgram

# colors = colorgram.extract('image.jpg', 6)  # Extract 6 colors from the image in the form of a list of Color objects

# rgb_colors = []
# for color in colors:
#     rgb = color.rgb # it gives an object of type Rgb with attributes r, g, b e.g., Rgb(r=245, g=245, b=220) 
#     rgb_colors.append((rgb.r, rgb.g, rgb.b))

#     # now would use this colors list to create a cologram or hirst painting

import turtle as turtle_module
import random

tim=turtle_module.Turtle()
turtle_module.colormode(255)  # Set the color mode to RGB
color_list=[(235, 234, 231), (234, 229, 232), (236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232)]

# can draw a dot with a specific color and radius
# to start the turtle at a specific position like a down left corner then we use 
tim.penup()  # Lift the pen to avoid drawing while moving to the starting position
tim.setheading(225)  # Set the heading to 225 degrees
tim.forward(300)  # Move forward by 300 units to start at the bottom left corner
tim.setheading(0)  # Reset the heading to 0 degrees (facing right). Now the turtle is at the bottom left corner
tim.speed("fastest")  # Set the drawing speed to the fastest

tim.hideturtle()  # Hide the turtle cursor for a cleaner look
number_of_dots = 100  # Total number of dots to draw


for dot_count in range(1,number_of_dots+1):  # Draw 100 dots
    tim.dot(20, random.choice(color_list))  # Draw a dot with radius 20 and color from the list
    tim.forward(50)  # Move forward by 50 units
    

    if dot_count % 10 == 0:  # After every 10 dots, move to the next row
        tim.setheading(90)  # Set the heading to 90 degrees (facing up)
        tim.forward(50)  # Move forward by 50 units to start at the top left corner
        tim.setheading(180)  # Reset the heading to 180 degrees (facing left)
        tim.forward(500)  # Move back to the left edge of the screen
        tim.setheading(0)  # Reset the heading to 0 degrees (facing right)



screen = turtle_module.Screen()
screen.exitonclick()  # Wait for a click to close the window