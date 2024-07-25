import random

file = open("W.txt","r")
words = file.read().upper()
WORDCHOICES = words.split("\n")
file.close()

class Wordle:
    def __init__(self):
        self.Word = random.choice(WORDCHOICES).upper()
        self.Guesses = 0
        self.WrongMessage = {"Green":[0,[],""],"Yellow":[0,""],"Red":[0,""]}
    
    def Check_Guess(self,guess):
        self.Guesses += 1
        if guess.upper() == self.Word:return f"Correct!. The word was {self.Word}"
        else:
            for index,i in enumerate(self.Word): self.Check_Letter(i,index)
            return "Incorrect"
    
    def Check_Letter(self,letter:str,pos:int):
        if letter == self.Word[pos]: 
            self.WrongMessage["Green"] = [self.WrongMessage["Green"][0] + 1,self.WrongMessage["Green"][1].append(pos),self.WrongMessage["Green"][2] + letter]
        elif letter in self.Word and ((letter not in self.WrongMessage["Yellow"][2] and letter not in self.WrongMessage["Green"][2]) or self.Word.count(letter) > 2): 
            self.WrongMessage["Yellow"] = [self.WrongMessage["Yellow"][0] + 1,self.WrongMessage["Yellow"][1].append(pos),self.WrongMessage["Yellow"][2] + letter]
        else:
            self.WrongMessage["Red"] = [self.WrongMessage["Red"][0] + 1,self.WrongMessage["Red"][1].append(pos),self.WrongMessage["Red"][2] + letter]
    
    def Display_Green(self):
        if self.WrongMessage["Green"][0] > 0:
            pass

