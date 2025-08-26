from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time 
from scoreboard import Scoreboard



# Setting up the screen first of 600*800 dimesion and black background color 
screen = Screen() 
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0) # tracer method controls the animation on the screen ( now to don't show the  paddle getting moved to 350,0 every time from center we will use it )
# currently won't even show the paddle because when we turn off the animation we have to manually update the screen and refresh it everytime for that will make a while loop


# making a separate left and right paddle using the Paddle class defined in other program but need to define the location of right and left paddle 
# separately because they are on the opposite ends of the screen
r_paddle=Paddle((350,0)) # passing the position of both paddles in the form of tuple 
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()


#Creating a paddle(bar for playing the grade )
# paddle = Turtle()
# paddle.shape("square") #all turtles start at 20*20 ( need to strech it along width by 5 and leave as it is along length)
# paddle.color("white") # to make sure the paddle is visible when we actually run the code 
# paddle.shapesize(stretch_wid=5,stretch_len=1) 
# paddle.penup() # in order to make the paddle go to the right boundary of the screen first need to penup and then use goto function 
# paddle.goto(350,0) # 350 along the x axis and 0 along the y axis


# def go_up():
#     # will gonna move the paddle to new position (by moving in y dirn only on clicking up arrow key and keeping x position constant)
#     new_y=paddle.ycor()+20 # will gonna move 20 positions up in the y axis 
#     paddle.goto(paddle.xcor(),new_y) # kept the current paddle x cordinate same but changed only the y cordinate 


# def go_down():
#     new_y=paddle.ycor()-20 # going 20 positions down 
#     paddle.goto(paddle.xcor(),new_y)




# To listen to the keystrokes 
screen.listen()
screen.onkey(r_paddle.go_up,"Up") # instead of plain passing go_up and go_down use right_paddle and left_paddle to access those methods 
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w") # instead of plain passing go_up and go_down use right_paddle and left_paddle to access those methods 
screen.onkey(l_paddle.go_down,"s") # using different keys for moving left paddle up and down using W and S




game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) # for slowing down the movement of ball by pausing the  loop during each iteration 
    screen.update() # while the game is on update the screen every single time for showing up the paddle at 350,0 and not showing its movement from the center of screen
    ball.move() # going to move the ball everytime the screen refreshes 

    # Detect collision with the wall
    # the screen is 800*600 so 300 each side of origin on y axis and 400 on x axis so if the ball had crossed these parameters then it had a collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y() # under these conditions making the ball to bounce 

    # Detect collision of the ball with the paddle for that need to make sure that distance between the ball and paddle is less than 20 and had to make sure it
    # is in the appropiate distance from the center of paddle as the distance method calculate distance from centers of both obbject so ball can touch at top of paddle 
    # also and there it would cross the distance as more than 20 but won't be able to detact it with just distance less than  20 condition so need to make sure 
    # that ball is in the lenght of the paddle also ( check if the ball has crossed by a certain point on x axis and it is at 50 distance from the paddle )

    if ball.distance(r_paddle)<50 and  ball.xcor()>320 or ball.distance(l_paddle)<50 and  ball.xcor()<-320:
        # ball has hit the right paddle  
        # now would bounce along the horizontal earlier were bouncing along the vertical 
        ball.bounce_x()

    # Detect when the ball misses any of the paddle that should restart the game 
    # width of the screen is 800(400 on both sides) we know paddle is at 350 so if the ball crosses 380 then its had missed the paddel

    # right paddle miss 
    if ball.xcor()>380:
        ball.reset_position()
        #when the right paddle player misses then its the point to left paddle player and vice versa
        scoreboard.l_point()

    # left paddle miss
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()