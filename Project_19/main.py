from turtle import Turtle, Screen
from snake import Snake 
from food import Food 
from scoreboard import Scoreboard
import time 

screen = Screen()
screen.title("Snake Game") # Set the title of the game window
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)  # Turn off the screen updates for smoother animation 

snake = Snake() # creating a snake object from the snake class 
food=Food() # object of food class 
scoreboard=Scoreboard()


# now will control the snake movement using the keys up down left right 
screen.listen() # start listening the keystrokes 
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down") # function binding to is the function in snake object with the same name 
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right") # these keys are define like this only with the first letter as capital 

game_is_on = True  # Variable to control the game loop
while game_is_on:
    screen.update()  # Update the screen to reflect changes
    time.sleep(0.1)  # Pause for a short duration to control the speed of the game (while the game is on the scteen will uupdate every 0.1 sec)
    
    snake.move() # every time screen refreshes we are moving the snake by one step using the method in the snake class

    #Detect snake collision with the food using the distance method in turtle class which can help in detecting distance between two turtle (snake and food)
    if snake.segments[0].distance(food)<15:
        # food is 10*10 so considering that if the snake is in the given distance with the food then both have collided
        # print("nom nom nom") 
        food.refresh() # when both collides the food is spawning to the next random location (can set the intensity of collision upto what distance we consider both colliding 
        # by changing the above distance of 15)

        snake.extend()
        scoreboard.increase_score() # increasing the score whenever the snakes collide 

    # Detect collision with the wall (snake is 20*20 so creating a 280*280 for reference around the screen past which we assume snake hit the wall)
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        game_is_on=False # game over when crashed into wall 
        scoreboard.game_over()

    #Detect collision of snake head with tail 
    #if head collides with any segment in tail then trigger game over sequence 
    for segment in snake.segments:
        if segment==snake.segments[0]:
            pass 
            # the first segment in the for loop would come as snake head only and it would be obviously at less distance than 10 from itself so to avoid game over at start pass the head segment in the for loop
        elif snake.segments[0].distance(segment)<10:
            # if the snake head distance from any of the sequence is less than 10 means the snake has collided with its tail
            game_is_on=False
            scoreboard.game_over()

    # or can write for skipping only the first element by slicing the  list
    # for segment in snake.segments[1:]:
    # #   if snake.segments[0].distance(segment)<10:
    #         # if the snake head distance from any of the sequence is less than 10 means the snake has collided with its tail
    #         game_is_on=False
    #         scoreboard.game_over()
 
    



screen.exitonclick()  # Wait for a click to close the window 