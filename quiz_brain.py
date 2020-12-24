import random

class Brain:
    def __init__(self, bank):
        self.bank = bank
    
    def ask_question(self):
        question = random.choice(self.bank)



