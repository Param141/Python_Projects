from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white") # scoreboard being given the white color 
        self.penup() # for not drawing 
        self.hideturtle() # want its turtle to be hidden because we are only interested in it being able to write something 
        self.l_score=0
        self.r_score=0 # defined attributes to keep a track of how the both players are playing 
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear() # for preventing overwriting of the points over each other and each time the screen gets clear and show new points 
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Courier",80,"normal")) # if only written this then at the center of the screen so shifted it at top 
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("Courier",80,"normal"))
    
    def l_point(self):
        self.l_score+=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score+=1
        self.update_scoreboard()