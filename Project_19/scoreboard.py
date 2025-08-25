# will gonna make a scoreboard also in the turtle form 
from turtle import Turtle 

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0 # to keep the track of the score 
        self.color("white") # currently the scoreboard is black by default so need to give it a visiible color before actually writing the text 
        self.penup() # need to write before sending the turtle text up to a new location otherwise a line shown of it going and representing path
        self.goto(0,270) # setting the turtle position to the top center of the screen ( need to be done before writing the text )
        
        self.update_scoreboard() # made a separate function to prevent the score getting overwritten on the  same place each time 
        # self.write(f"The Score is {self.score}",align="center",font=("Arial,24,normal")) # read how the write method works in turtle class 
        # takes 3 argument first what to show, second where to align it , and third is what should be its font like in the tuple form (font,size,style)
        self.hideturtle() # one arrow comes when we show the scoreboard of turtle to  make it disappear use this 

    def update_scoreboard(self):
        self.write(f"Score:{self.score}",align="center",font=("Courier,24,normal"))
    
    def game_over(self):
        self.goto(0,0) # showing the game over text at the center of the screen 
        self.write("GAME OVER",align="center",font=("Courier,24,normal"))

    def increase_score(self):
        # writing a method to update the score whenever the snake collides with the ball and writing the text 
        self.score+=1
        self.clear() # need to clear the previous text written on the screenboard before writing the new score otherwise both overlaps 
        self.update_scoreboard()
