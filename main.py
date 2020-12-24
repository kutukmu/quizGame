from data import question_data

from question_model import Question



question_bank = [Question(item['text'], item['answer']) for item in data]