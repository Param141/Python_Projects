class Question:
    def __init__(self,q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


new_q = Question("What is the capital of France?", "Paris")
print(new_q.text)  # Output: What is the capital of France?
print(new_q.answer)  # Output: Paris