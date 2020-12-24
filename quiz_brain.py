import random

class Brain:

    def __init__(self, bank):
        self.bank = bank
        self.question_number = 0
    
    def next_question(self):
        ask  = self.bank[self.question_number]
        answer  = input(f'Q{self.question_number + 1}: {ask.text} (True / False)?')
        self.question_number += 1
        


    def checkAnwer(self , answer):
        ans = self.question.answer
        if ans == answer:
            print('Good Job You won')
        else:
            print('Wrong Answer')
    


