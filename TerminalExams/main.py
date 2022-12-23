from question_model import Question
from data import question_data

question_bank = []
number = 0
for i in range(len(question_data)):
    question = question_data[i]["text"]
    answer = question_data[i]["answer"]
    question_bank.append(Question(question, answer))

print(question_bank[1].question)