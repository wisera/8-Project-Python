# Project 3
# objective: create an algorithm that generates a random value and I have to keep on guessing until I get it right

import random

class GuessTheNumber:
    def __init__(self):
        self.random_value = 0
        self.max_value = 100
        self.min_value = 1
        self.try_again = True

    def Start(self):
        self.GenerateRandomNumber()
        self.AskForRandomNumber()
        try:
            while self.try_again == True:
                if int(self.guess_value) > self.random_value:
                    print('Guess a smaller number')
                    self.AskForRandomNumber()
                elif int(self.guess_value) < self.random_value:
                    print('Guess a bigger number')
                    self.AskForRandomNumber()
                if int(self.guess_value) == self.random_value:
                    self.try_again = False
                    print('Congrats you guessed it!')
        except:
            print('Please only enter numbers!')
            self.Start()
    
    def AskForRandomNumber(self):
        self.guess_value = input('Guess a number: ')

    def GenerateRandomNumber(self):
        self.random_value = random.randint(self.min_value, self.max_value)
game = GuessTheNumber()
game.Start()
