import random

file = open("W.txt","r")
words = file.read().upper()
WORDCHOICES = words.split("\n")
file.close()

class Wordle:
    def __init__(self):
        self.Word = random.choice(WORDCHOICES).upper()
        self.Guesses = 0
        self.WrongMessage = {"Green":[0,""],"Yellow":[0,""],"Red":[0,""]}
    
    def Check_Guess(self,guess):
        self.Guesses += 1
        if guess.upper() == self.Word:return f"Correct!. The word was {self.Word}"
        else:
            pass
    
    def Check_Letter(self,letter,pos):
        pass