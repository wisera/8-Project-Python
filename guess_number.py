# Project 3
# objective: create an algorithm that generates a random value and I have to keep on guessing until I get it right

import random
import PySimpleGUI as sg
class GuessTheNumber:
    def __init__(self):
        self.random_value = 0
        self.max_value = 100
        self.min_value = 1
        self.try_again = True
        

    def Start(self):
        # Layout
        layout = [
            [sg.Text('Your Guess', size=(30,0))],
            [sg.Input(size=(18,0), key='GuessValue')],
            [sg.Button('Guess!')],
            [sg.Output(size=(30,10))]
        ]
        # create window
        self.window = sg.Window('Guess a number!',layout=layout)
        self.GenerateRandomNumber()
        try:
            while True:
                # receive values
                self.event, self.values = self.window.Read()
                # do something w/ these values
                if self.event == 'Guess!':
                    self.guess_value = self.values['GuessValue']
                    while self.try_again == True:
                        if int(self.guess_value) > self.random_value:
                            print('Guess a smaller number')
                            break
                        elif int(self.guess_value) < self.random_value:
                            print('Guess a bigger number')
                            break
                        if int(self.guess_value) == self.random_value:
                            self.try_again = False
                            print('Congrats you guessed it!')
                            break
        except:
            print('Please only enter numbers!')
            self.Start()

    def GenerateRandomNumber(self):
        self.random_value = random.randint(self.min_value, self.max_value)
game = GuessTheNumber()
game.Start()
