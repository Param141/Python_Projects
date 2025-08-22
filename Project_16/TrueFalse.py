from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list of Question objects from the question_data
question_bank = []
for question in question_data:
    question_text = question['text'] # Extract the question text from the dictionary
    question_answer = question['answer']
    new_question = Question(question_text, question_answer) # Create a new Question object 
    question_bank.append(new_question) # Add the Question object to the question_bank list

# print(question_bank[0].text)  # Output: A slug's blood is green.
# print(question_bank[0].answer)  # Output: True

quiz=QuizBrain(question_bank)

while quiz.still_has_question:
    quiz.next_question()


print("You have completed the  quiz")
print(f"Your final score was : 1{quiz.score}/{quiz.question_number}") # or can use len(question_bank) also in the denominator