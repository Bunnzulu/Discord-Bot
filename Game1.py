import random
import time
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
        self.AIGuesses = 0
    
    def Pick_random_Number(self):
        self.Number = random.randint(self.LowNumber,self.HighNumber)
    
    def UserGuess(self,Guess:int) -> str:
        self.UserGuesses += 1
        if Guess > self.Number:return "Too High"
        if Guess == self.Number:
            self.NumberGuessed = True
            return "That's it"
        else:return "Too Low"
    
    def Reset(self,EndGame:bool=False):
        self.Number = 0
        self.NumberGuessed = False
        self.Turn = "Bot"
        if EndGame:
            self.AIHighNumber = 0
            self.AILowNumber = 0
            self.Turn = ""
            self.Active = False
            self.UserGuesses = 0
            self.AIGuesses = 0
            self.HighNumber = ""
            self.LowNumber = ""

    def AIGuess(self):
        time.sleep(5)
        self.AIGuesses += 1
        Guess = random.randint(self.AILowNumber,self.AIHighNumber)
        if Guess > self.Number:
            self.AIHighNumber = Guess - 1
            return f"{Guess}, No that's too high"
        elif Guess == self.Number:
            self.NumberGuessed = True
            return f"{Guess}, Got it!"
        else:
            self.AILowNumber = Guess + 1
            return f"{Guess}, No that's too low!"

    def Winner(self):
        if self.UserGuesses > self.AIGuesses: return "So I win!"
        elif self.UserGuesses < self.AIGuesses: return "So you win!"
        else:return "So it's a tie"

    def VerifyPickedNumber(self,num):
        if num > self.HighNumber or num < self.LowNumber: return False
        self.Number = num
        return True

def UserInput_StoN(message):
    result = int(message)
    return result
