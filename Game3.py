import random

QUESTIONBANK = ["Which planet is known as the Red Planet?","Who wrote 'Romeo and Juliet'?","What is the largest ocean on Earth?","How many Continents are there?",
    "Which element has the chemical symbol O?", "What is the smallest unit of life?","Who was the first president of the US?","What is the process by which plants make their food?",
    "Which instrument is used to mesure temperature?","What is the capital of France?","What is the largest planet in our solar system?","Who painted the Mona Lisa?",
    "What is the hardest natural substance on Earth?","Which country is known as the Land of the Rising Sun?","What is the smallest country in the world by land area?",
    "What is the main ingredient in traditional Japanese miso soup?","Which is the longest river in the world?","In which year did the Titanic sink?","What does the acronym 'WWW' stand for?",
    "Who is known as the Father of Computers?"]


QUESTIONSHEET = {
    "What is the capital of France?":["Berlin","Madrid","Rome","Paris"],
    "Which planet is known as the Red Planet?":["Earth","Mars","Jupiter","Venus"],
    "Who wrote 'Romeo and Juliet'?":["William Shakespeare","Charles Dickens","J.K. Rowling","Mark Twain"],
    "What is the largest ocean on Earth?":["Atlantic Ocean","Indian Ocean","Arctic Ocean","Pacific Ocean"],
    "How many Continents are there?":["5","6","7","8"],
    "Which element has the chemical symbol O?":["Gold","Oxygen","Silver","Iron"],
    "What is the smallest unit of life?":["Atom","Molecule","Cell","Organism"],
    "Who was the first president of the US?":["Abraham Lincoln","George Washington","Thomas Jefferson","John Adams"],
    "What is the process by which plants make their food?":["Respiration","Digestion","Photosynthesis","Fermentation"],
    "Which instrument is used to mesure temperature?":["Barometer","Hygrometer","Thermometer","Anemometer"],
    "What is the largest planet in our solar system?":["Earth","Jupiter","Saturn","Neptune"],
    "Who painted the Mona Lisa?":["Vincent van Gogh","Pablo Picasso","Leonardo da Vinci","Claude Monet"],
    "What is the hardest natural substance on Earth?":["Gold","Iron","Diamond","Silver"],
    "Which country is known as the Land of the Rising Sun?":["China","Japan","India","South Korea"],
    "What is the smallest country in the world by land area?":["Monaco","Vatican City","San Marino","Liechtenstein"],
    "What is the main ingredient in traditional Japanese miso soup?":["Tofu","Seaweed","Miso paste","Rice"],
    "Which is the longest river in the world?":["Amazon River","Nile River","Yangtze River","Mississippi River"],
    "In which year did the Titanic sink?":["1905","1912","1923","1930"],
    "What does the acronym 'WWW' stand for?":["World Wide Web","World Wide Wind","Wide World Web","Web World Wide"],
    "Who is known as the Father of Computers?":["Alan Turing","Charles Babbage","Thomas Edison","Bill Gates"]
}

ANSWERSHEET = {
    "What is the capital of France?":"Paris",
    "Which planet is known as the Red Planet?":"Mars",
    "Who wrote 'Romeo and Juliet'?":"William Shakespeare",
    "What is the largest ocean on Earth?":"Pacific Ocean",
    "How many Continents are there?": "7",
    "Which element has the chemical symbol O?": "Oxygen",
    "What is the smallest unit of life?": "Cell",
    "Who was the first president of the US?": "George Washington",
    "What is the process by which plants make their food?": "Photosynthesis",
    "Which instrument is used to mesure temperature?": "Thermometer",
    "What is the largest planet in our solar system?":"Jupiter",
    "Who painted the Mona Lisa?":"Leonardo da Vinci",
    "What is the hardest natural substance on Earth?":"Diamond",
    "Which country is known as the Land of the Rising Sun?":"Japan",
    "What is the smallest country in the world by land area?":"Vatican City",
    "What is the main ingredient in traditional Japanese miso soup?":"Miso paste",
    "Which is the longest river in the world?":"Nile River",
    "In which year did the Titanic sink?":"1912",
    "What does the acronym 'WWW' stand for?":"World Wide Web",
    "Who is known as the Father of Computers?":"Charles Babbage"
}

class Quiz:
    def __init__(self):
        self.Score = 0
        self.QNumber = 1
        self.Active = False
        self.Question = ""
        self.Answered = False
        self.Complete = False
        self.Answers = []
        self.UsedQuestions =[]
    
    def GetQuestion(self):
        self.Question = random.choice(QUESTIONBANK)
        while self.Question in self.UsedQuestions:self.Question = random.choice(QUESTIONBANK)
        self.Answers = QUESTIONSHEET[self.Question]
        self.UsedQuestions.append(self.Question)
    
    def ShowQuestion(self):
        return f"Question {self.QNumber}: {self.Question}\n{self.Answers[0]}\n{self.Answers[1]}\n{self.Answers[2]}\n{self.Answers[3]}"
    
    def CheckAnswer(self,Guess):
        if Guess not in self.Answers: return "Not an option"
        else:
            self.Answered = True
            self.QNumber += 1
            if Guess == ANSWERSHEET[self.Question]: 
                self.Score += 1
                return "Correct"
            else: return f"Incorrect, the right answer was {ANSWERSHEET[self.Question]}"
    
    
    def Reset(self):
        self.Score = 0
        self.QNumber = 1
        self.Active = False
        self.Question = ""
        self.Answered = False
        self.Complete = False
        self.Answers = []
        self.UsedQuestions =[]