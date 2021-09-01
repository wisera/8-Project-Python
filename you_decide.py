# Project 5 - Decide for me
# Ask a question and Python will naswer it for you
import random

class YouDecide:
    def __init__(self):
        self.answers = [
            'Of course, you should do it!',
            'I dont know, you decide',
            'NO! Dont do it!',
            'I think this is the right time'
        ]

    def Start(self):
        input('Ask your question: ')
        print(random.choice(self.answers))

decide = YouDecide()
decide.Start()