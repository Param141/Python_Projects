from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup() # so that it doesn't end up drawing its path in the form of line on the screen
        self.x_move=10
        self.y_move=10 # setting up variable separately for moving the ball 
        self.move_speed=0.1 # making a variable to increase the speed of ball each time anyone scores the point 

    def move(self): # for moving the ball across the screen 
        new_x=self.xcor()+self.x_move # each time the screen update the ball is moving by 10 if want to slow down then keep it as 1 
        new_y=self.ycor()+self.y_move # each time would move by 10 units when the key is pressed
        self.goto(new_x,new_y)

    def bounce_y(self):
        # for bouncing the ball
        # for that need to reverse the previous coordinates like if the y coordinate was increasing earlier now it needs to decrease and vice versa
        self.y_move*=-1 # multiplying with -1 in order to inverse the  sign of y to move it oppositely as now new_y=self.ycor()-self.ycor()

    def bounce_x(self):
        self.x_move*=-1
        # ball getting bounced in x dirn means touched by a paddle so increase the moving speed further ( make sure while decreasing it you don't make it negative 1)
        self.move_speed*=0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x() # when the ball missess the padel of one side let suppose right then it would start again from the intial position and now would go towards the other 
        # paddel which is left paddel ( reversing the x axis of the ball) 
        # when one player had lost then we had to again reset the ball speed to normal


    