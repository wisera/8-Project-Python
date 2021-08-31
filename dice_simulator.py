# Dice SIMULATOR
# Simulate a dice, generating a value from 1 to 6
import random
import PySimpleGUI as sg

class DiceSimulator:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        self.message = "Would like to generate a new value for the dice?"
        # layout
        self.layout = [
            [sg.Text('Roll dice?')],
            [sg.Button('yes'),sg.Button('no')]
        ]
       
    def Start(self):
        # create a window
        self.window = sg.Window('Dice Simulator',self.layout)
        # read values on screen
        self.events, self.values = self.window.Read()
        # do something w/ values
        try:
            if self.events == 'yes' or self.events == 'y':
                self.GenerateDiceValue()
            elif self.events =='no' or self.events == 'n':
                print('Thanks for your participation!')
            else:
                print('Please enter yes or no')
        except:
            print('Theres an wrror in your answer')
    def GenerateDiceValue(self):
        print(random.randint(self.min_value, self.max_value))

simulador = DiceSimulator()
simulador.Start()