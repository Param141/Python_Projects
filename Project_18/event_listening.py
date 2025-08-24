from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


# in order to listen for key presses, we need to call the listen() method on the screen 
screen.listen() # and once it starts listening we have to bind the key presses to functions which would be called when the key is pressed
screen.onkey(key="space", fun=move_forward)  # when the "space" key is pressed, the move_forward function will be called.Here onkey is event listener
# when we pass the function as an argument, we don't include the parentheses because we don't want to call the function immediately, we want it to be called when the key is pressed.
screen.exitonclick()  # this will close the screen when we click on it

