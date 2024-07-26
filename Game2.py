import random

file = open("W.txt","r")
words = file.read().upper()
WORDCHOICES = words.split("\n")
file.close()

class Wordle:
    def __init__(self):
        self.Active = False
        self.Word = "STEEL"#random.choice(WORDCHOICES).upper()
        self.Guesses = 6
        self.GuessCorrect = False
        self.WrongMessage = {"Green":[0,[],""],"Yellow":[0,[],""],"Red":[0,[],""]}
    
    def Check_Guess(self,guess):
        self.Guesses -= 1
        if guess.upper() == self.Word:
            self.GuessCorrect = True
            return f"Correct!. The word was {self.Word}"
        else:
            for index,i in enumerate(guess.upper()): self.Check_Letter(i,index)
            return "Incorrect"
        
    def Check_Letter(self,letter:str,pos:int):
        if letter == self.Word[pos]: 
            self.WrongMessage["Green"][0] += 1
            self.WrongMessage["Green"][1].append(pos + 1)
            self.WrongMessage["Green"][2] += letter
        elif letter in self.Word and (self.WrongMessage["Yellow"][2].count(letter) + self.WrongMessage["Green"][2].count(letter)) < self.Word.count(letter): 
            self.WrongMessage["Yellow"][0] += 1
            self.WrongMessage["Yellow"][1].append(pos + 1)
            self.WrongMessage["Yellow"][2] += letter
        else:
            self.WrongMessage["Red"][0] += 1
            self.WrongMessage["Red"][1].append(pos + 1)
            self.WrongMessage["Red"][2] += letter
    
    def Display_Green(self):
        if self.WrongMessage["Green"][0] > 0:
            return "The right letters in the right spot are",self.WrongMessage["Green"][1]
        else: return "No right letters are in right positions"
    
    def Display_Yellow(self):
        if self.WrongMessage["Yellow"][0] > 0:
            return "The right letters in the wrong spot are",self.WrongMessage["Yellow"][1]
        else: return "No right letters are in wrong positions"

    def Display_Red(self):
        if self.WrongMessage["Red"][0] > 0:
            return "The wrong letters are",self.WrongMessage["Red"][1]
        else: return "No wrong letters are here"

    def Random_Word(self):
        self.Word = random.choice(WORDCHOICES).upper()
        self.Guesses = 0
        self.WrongMessage = {"Green":[0,[],""],"Yellow":[0,""],"Red":[0,""]}

    def Valid_Word(self,Word):
        if Word.upper() in WORDCHOICES: return True
        else: return False