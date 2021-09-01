# Project 5 - Decide for me
# Ask a question and Python will naswer it for you
import random
import PySimpleGUI as sg
class YouDecide:
    def __init__(self):
        self.answers = [
            'Of course, you should do it!',
            'I dont know, you decide',
            'NO! Dont do it!',
            'I think this is the right time'
        ]

    def Start(self):
        # Layout
        layout = [
            [sg.Text('Ask your Question: ')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('You Decide')]
        ]
        # Window
        self.window = sg.Window('You Decide!', layout=layout)
        while True:
            # Read values
            self.events, self.values = self.window.Read()
            # Do something w/ values
            if self.events == 'You Decide':
                print(random.choice(self.answers))

decide = YouDecide()
decide.Start()