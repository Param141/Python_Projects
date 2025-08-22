# here will gonna do two things 
# TODO : asking the questions from the user and checking the answer 
# TODO : checking if we are at the end of the quiz or not

class QuizBrain:
    def __init__(self,q_list): # attributes of Question ojects which are items in the list 
        self.question_number=0
        self.score=0
        self.question_list=q_list

    def still_has_question(self):
        if self.question_number<len(self.question_list):
            return True # still the questions are left in the question list 
        else:
            return False # no questions left 
        
        # or simply return question_number < len(self.question_list)

    def next_question(self):
        current_question=self.question_list[self.question_number] # getting the current question by tapping onto the question list and going at current question number 
        # correct_question.text can get hold of current question text 
        self.question_number+=1 # in order to increase the question number each time and start from 1st question instead of 0
        user_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)
    
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("You got it right !")
        else:
            print("That's wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
