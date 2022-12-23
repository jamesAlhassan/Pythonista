class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __repr__(self):
        return f"{self.question} ({self.answer}/false)"


# question_1 = Question("What is the brain of the computer? ", "CPU")
