import discord 
from dotenv import load_dotenv
import os
import re
from Game1 import NumberGuesserGame,UserInput_StoN
from Game2 import Wordle
from Game3 import Quiz
load_dotenv(".env")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

GuessingGame = {}
wordle = {}
quiz = {}

def MultiCheck(user_id,Groups):
    for group in Groups:
        if user_id in group and group[user_id].Active: return False
    return True

ChosenChannel = "ChannelName"

@client.event
async def on_ready():
    channels = list(client.get_all_channels())
    print(f'We have logged in as {client.user}')
    for channel in channels:
        if channel.name == ChosenChannel:
            await channel.send("Commands: $Hello, $GuessingGame, $Wordle, $Quiz")

@client.event
async def on_message(message):
    user_id = message.author.id
    if message.author == client.user:
        return

    if message.content.startswith('$Hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$GuessingGame') and MultiCheck(user_id,[GuessingGame,wordle,quiz]):
        if user_id not in GuessingGame or not GuessingGame[user_id].Active:
            GuessingGame[user_id] = NumberGuesserGame()
            GuessingGame[user_id].Active = True
            GuessingGame[user_id].Turn = "User"
            await message.channel.send(f'{message.author.mention}, Pick how high the number can go\n(Highest number is 999)\n $Number')
        else:
            await message.channel.send(f'{message.author.mention}, you already have an active game.')
    
    if message.content.startswith('$Wordle') and MultiCheck(user_id,[GuessingGame,wordle,quiz]):
        if user_id not in wordle or not wordle[user_id].Active:
            wordle[user_id] = Wordle()
            wordle[user_id].Active = True
            await message.channel.send(f"{message.author.mention}, let's play")
            await message.channel.send("Hint: Start guessing 5-letter words, start with $\n $Guess")
            await message.channel.send("Type $ShowGuess to see how many attempts you have left.")
    
    if message.content.startswith('$Quiz') and MultiCheck(user_id,[GuessingGame,wordle,quiz]):
        quiz[user_id] = Quiz()
        quiz[user_id].Active = True
        quiz[user_id].GetQuestion()
        await message.channel.send(f"Quiz is starting")
        await message.channel.send(f"{message.author.mention}\n {quiz[user_id].ShowQuestion()}")
        await message.channel.send("Type $(YourAnswerhere) to answer question")
    
    elif user_id in GuessingGame and GuessingGame[user_id].Active:
        if GuessingGame[user_id].Turn == "User":
            if message.content.startswith('$'):
                if not message.content.startswith('$0') and GuessingGame[user_id].LowNumber == "":
                    if len(re.findall(r'\d{1,3}',message.content)):
                        if GuessingGame[user_id].HighNumber == "": 
                            GuessingGame[user_id].HighNumber = UserInput_StoN(re.findall(r'\d{1,3}',message.content)[0])
                            await message.channel.send(f'{message.author.mention}, Pick how low the number can go\n(Lowest number is 1)')
                        elif GuessingGame[user_id].LowNumber == "": 
                            GuessingGame[user_id].LowNumber = UserInput_StoN(re.findall(r'\d{1,3}',message.content)[0])
                            await message.channel.send(f"{message.author.mention}, Let's play")
                            GuessingGame[user_id].Pick_random_Number()
                            await message.channel.send(f"{message.author.mention}, Highest Number: {GuessingGame[user_id].HighNumber} and Lowest Number: {GuessingGame[user_id].LowNumber}")
                            await message.channel.send(f"{message.author.mention}, Start guessing")
                elif not GuessingGame[user_id].NumberGuessed and "" not in (GuessingGame[user_id].HighNumber,GuessingGame[user_id].LowNumber):
                    if len(re.findall(r'\d{1,3}',message.content)):
                        await message.channel.send(GuessingGame[user_id].UserGuess(UserInput_StoN(re.findall(r'\d{1,3}',message.content)[0])))
                        await message.channel.send(f"{message.author.mention}, Guesses made:{GuessingGame[user_id].UserGuesses}")
                        if GuessingGame[user_id].NumberGuessed:
                            await message.channel.send(f"{message.author.mention},Now it's my turn")
                            await message.channel.send(f"{message.author.mention}, Pick your number")
                            GuessingGame[user_id].Reset()
        elif GuessingGame[user_id].Turn == "Bot":
            if message.content.startswith('$'):
                if GuessingGame[user_id].AIHighNumber == 0 and not message.content.startswith('$0'):
                    if GuessingGame[user_id].VerifyPickedNumber(UserInput_StoN(re.findall(r'\d{1,3}',message.content)[0])):
                        GuessingGame[user_id].AIHighNumber = GuessingGame[user_id].HighNumber
                        GuessingGame[user_id].AILowNumber = GuessingGame[user_id].LowNumber
                        await message.channel.send("I'm going to start guessing")
                        await message.channel.send(f"{message.author.mention}, Hint: type $BotGuess to continue")
                    else:
                        await message.channel.send(f"{message.author.mention}, Invalid Input")
                        await message.channel.send(f"{message.author.mention}, Highest Number:{GuessingGame[user_id].HighNumber} and Lowest Number:{GuessingGame[user_id].LowNumber}")
                elif message.content.startswith('$BotGuess'):
                    while not GuessingGame[user_id].NumberGuessed:
                        await message.channel.send(GuessingGame[user_id].AIGuess())
                    await message.channel.send(f"{message.author.mention}, You took {GuessingGame[user_id].UserGuesses} guesses and I took {GuessingGame[user_id].AIGuesses} guesses")
                    await message.channel.send(GuessingGame[user_id].Winner())
                    await message.channel.send(f"{message.author.mention}, Game over!")
                    GuessingGame[user_id].Reset(True)

    elif user_id in wordle and wordle[user_id].Active:
        if message.content.startswith('$'):
            if message.content.startswith("$ShowGuess"):await message.channel.send(f"You have {wordle[user_id].Guesses} guesses left")
            if len(message.content) == 6 and not wordle[user_id].GuessCorrect and wordle[user_id].Guesses > 0:
                if wordle[user_id].Valid_Word(message.content[1:]):
                    await message.channel.send(wordle[user_id].Check_Guess(message.content[1:]))
                    if not wordle[user_id].GuessCorrect:
                        await message.channel.send(message.author.mention)
                        await message.channel.send(wordle[user_id].Display_Green())
                        await message.channel.send(wordle[user_id].Display_Yellow())
                        await message.channel.send(wordle[user_id].Display_Red())
                        wordle[user_id].WrongMessage = {"Green":[0,[],""],"Yellow":[0,[],""],"Red":[0,[],""]}
                    else:
                        await message.channel.send("Thanks for playing")
                        wordle[user_id].Active = False
                else:await message.channel.send("Invalid word")
            if wordle[user_id].Guesses == 0:
                await message.channel.send(f"The word was {wordle[user_id].Word}")
                await message.channel.send("Thanks for playing")
                wordle[user_id].Reset()
    
    elif user_id in quiz and quiz[user_id].Active:
        if message.content.startswith('$'):
            await message.channel.send(f"{message.author.mention},{quiz[user_id].CheckAnswer(message.content[1:])}")
            if quiz[user_id].Answered: 
                quiz[user_id].Answered = False
                if quiz[user_id].QNumber == 11: quiz[user_id].Complete = True
                else:
                    quiz[user_id].GetQuestion()
                    await message.channel.send(f"{message.author.mention}\n {quiz[user_id].ShowQuestion()}")
            if quiz[user_id].Complete:
                await message.channel.send(f"{message.author.mention},Quiz complete\n Score:{quiz[user_id].Score}/10")
                quiz[user_id].Reset()

client.run(os.getenv("TOKEN"))