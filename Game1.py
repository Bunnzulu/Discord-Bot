import random

class NumberGuesserGame():
    def __init__(self):
        self.HighNumber = ""
        self.LowNumber = ""
        self.Number = 0
        self.AIHighNumber = 0
        self.AILowNumber = 0
        self.Turn = ""
        self.NumberGuessed = False
        self.Active = False
        self.UserGuesses = 0
    
    def Pick_random_Number(self):
        self.Number = random.randint(self.LowNumber,self.HighNumber)
    
    def UserGuess(self,Guess:int) -> str:
        self.UserGuesses += 1
        if Guess > self.Number:return "Too High"
        if Guess == self.Number:return "That's it"
        else:return "Too Low"
    

def UserInput_StoN(message):
    try:
        result = int(message[1:4])
    except:
        try:
            result = int(message[1:3])
        except:
            try:
                result = int(message[1:1])
            except:print(message)
    return result