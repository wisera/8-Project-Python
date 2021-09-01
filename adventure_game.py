 # Project 7 - Adventure Game
 # A game of decisions, where I will have to create multiple different possible scenarios based on the answers given
 # I want to reach different endings in my story, based on asnswers I give to Python

# Whats the scenario? Im in war between 2 nations, and we have 2 sides: A and B. Only side A will win, and side B will lose! So I have to take the right decisions in order to win

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
        answer1 = input(self.question1)
        if answer1 == 'n' :
            answer1B = input(self.question2)
            if answer1B == 'sword':
                print(self.finalStory1)
            if answer1B == 'shield':
                print(self.finalStory2)
        if answer1 == 's':
            answer1B = input(self.question3)
            if answer1B == 'entry':
                print(self.finalStory3)
            if answer1B == 'clutch':
                print(self.finalStory4)
                
game = AdventureGame()
game.Start()