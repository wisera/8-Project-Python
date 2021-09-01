 # Project 7 - Adventure Game
 # A game of decisions, where I will have to create multiple different possible scenarios based on the answers given
 # I want to reach different endings in my story, based on asnswers I give to Python

# Whats the scenario? Im in war between 2 nations, and we have 2 sides: A and B. Only side A will win, and side B will lose! So I have to take the right decisions in order to win
import PySimpleGUI as sg

class AdventureGame:
    def __init__(self):
        self.question1 = 'Where were you born, North or South? (n/s)' # north = A, south = B
        self.question2 = 'Do you prefer sword or shield? (sword/shield)' # sword = A, shield = B
        self.question3 = 'Whats your speciality? (entry/clutch)' # entry = A, # clutch = B
        self.finalStory1 = 'You are an entry fragger!'
        self.finalStory2 = 'You are a hero that will prtect our troops!'
        self.finalStory3 = 'You will sacrifice yourself in the battle!'
        self.finalStory4 = 'You are not capable of fighting this battle!'



    def Start(self):
        # Layout
        layout = [
            [sg.Output(size=(50,0), key='answers')],
            [sg.Input(size=(25,0), key='choose')],
            [sg.Button('Start'), sg.Button('Answer')]
        ]
        # create window
        self.window = sg.Window('Adventure Game!', layout=layout)
        while True:
            # read data
            self.ReadValues()
            # do something w/ data
            if self.event == 'Start':
                print(self.question1)
                self.ReadValues()
                if self.values['choose'] == 'n' :
                    print(self.question2)
                    self.ReadValues()
                    if self.values['choose'] == 'sword':
                        print(self.finalStory1)
                    if self.values['choose'] == 'shield':
                        print(self.finalStory2)
                if self.values['choose'] == 's':
                    print(self.question3)
                    self.ReadValues()
                    if self.values['choose'] == 'entry':
                        print(self.finalStory3)
                    if self.values['choose'] == 'clutch':
                        print(self.finalStory4)

    def ReadValues(self):
        self.event, self.values = self.window.Read()
game = AdventureGame()
game.Start()